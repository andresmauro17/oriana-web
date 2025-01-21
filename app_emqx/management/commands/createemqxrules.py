from django.core.management.base import BaseCommand
import os
import base64
import requests


class Command(BaseCommand):
    """ 
        this command creates the resources in emqx
        python manage.py createemqxrules
        docker-compose run --rm django python manage.py createemqxrules
    """
    help = 'this command creates the resources in emqx'

    EMQX_API_HOST = os.getenv('EMQX_API_HOST')
    AUTH_HEADER = "Basic " + base64.b64encode((os.getenv('EMQX_API_KEY') + ":" + os.getenv('EMQX_API_SECRET')).encode()).decode()

    def createCurrenDataToDjangoRule(self):
        """ createCurrenDataToDjangoRule """
        headers = {
            "Accept": "application/json",
            "Authorization": self.AUTH_HEADER
        }

        # creating bridge
        webhook_name = "current_data_to_django_webhook_6_1"
        webhook_id = f'webhook:{webhook_name}'
        body = {
            "type": "webhook",
            "name": webhook_name,
            "method": "post",
            "url": f'{os.getenv("WEBHOOKS_HOST")}/'+"${sensor_path}",
            "headers": {
                "Accept": "application/json",
                "content-type": "application/json",
            },
            "body": '{"deviceid":"${device_id}","value":${payload.value},"energy":${payload.energy}}',
            "pool_type": "random",
            "pool_size": 8,
            "enable_pipelining": 100,
            "connect_timeout": "15s",
            "request_timeout": "15s",
            "resource_opts": {
                "worker_pool_size": 4,
                "health_check_interval": "15s",
                "auto_restart_interval": "60s",
                "query_mode": "async",
                "max_queue_bytes": "1GB",
                "request_timeout": "15s",
                "async_inflight_window": 100
            },
            "ssl": {
                "enable": False,
                "verify": "verify_peer"
            }
        }
        exists_bridge = requests.get(f"{self.EMQX_API_HOST}/bridges/{webhook_id}", headers=headers)
        created_or_updated_str = ""
        if(exists_bridge):
            response = requests.put(f"{self.EMQX_API_HOST}/bridges/{webhook_id}", json=body, headers=headers)
            created_or_updated_str="updated"
        else:
            response = requests.post(f"{self.EMQX_API_HOST}/bridges/", json=body, headers=headers)
            created_or_updated_str="created"
        self.stdout.write(
            self.style.SUCCESS(f'Successfully bridge {webhook_id} {created_or_updated_str}!')
        )
        response_json = response.json()
        print(response_json)

        # creating rule
        rule_query = """
SELECT
   payload,
   find(topic, 'sensors/') as sensor_path,
   substr(topic, 8, 11) as device_id
FROM
  "devices/+/sensors/+/currentdata/"
        """
        rule_id = "current_device_sensor_data_to_django_6_1"
        body = {
            "id": rule_id,
            "name": rule_id,
            "sql": rule_query,
            "actions": [
                webhook_id,
            ],
            "enable": True,
            "description": "Send current data to django",
            "metadata": {}
        }

        exists_rule = requests.get(f"{self.EMQX_API_HOST}/rules/{rule_id}", headers=headers)
        created_or_updated_str = ""
        if(exists_rule):
            response = requests.put(f"{self.EMQX_API_HOST}/rules/{rule_id}", json=body, headers=headers)
            created_or_updated_str="updated"
        else:
            response = requests.post(f"{self.EMQX_API_HOST}/rules/", json=body, headers=headers)
            created_or_updated_str="created"
        response_json = response.json()
        self.stdout.write(
            self.style.SUCCESS(f'Successfully bridge {rule_id} {created_or_updated_str}!')
        )
        print(response_json)

    def handle(self, *args, **kwargs):
        self.createCurrenDataToDjangoRule()
        self.stdout.write(f'creating rule in emqx')
