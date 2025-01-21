""" Sensor services """

import os
import base64
import requests


def create_sensor_rule(sensor):
    """
    this funcition is to create or uodate the rule in emqx
    gixing the sensor_unique
    """
    rule_id = f"sensor_{sensor.id}"
    EMQX_API_HOST = os.getenv("EMQX_API_HOST")
    AUTH_HEADER = (
        "Basic "
        + base64.b64encode(
            (
                os.getenv("EMQX_API_KEY") + ":" + os.getenv("EMQX_API_SECRET")
            ).encode()
        ).decode()
    )
    headers = {"Accept": "application/json", "Authorization": AUTH_HEADER}

    # creating rule
    updated_at_millis = int(sensor.updated_at.timestamp() * 1000)
    rule_query = f"""
SELECT
   payload,
   topic
FROM
  "devices/{sensor.device.device_id}/sensors/{sensor.unique_id}/currentdata/"
WHERE payload.updated_att != {updated_at_millis} 
"""
    topic_response = (
        f"devices/{sensor.device.device_id}/config/{sensor.unique_id}/"
    )

    contacts = sensor.get_contacts()
    phones_string = ""
    index = 0
    if contacts['sms_numbers']:
        for phone in contacts['sms_numbers']:
            index += 1
            phones_string += f"{phones_string}|phone{index}:{phone}"

    payload_response = f"name:{sensor.name}|updated_at:{updated_at_millis}|max:{sensor.max_threshold}|min:{sensor.min_threshold}{phones_string}"
    body = {
        "id": rule_id,
        "name": rule_id,
        "sql": rule_query,
        "actions": [
            {
                "function": "republish",
                "args": {
                    "topic": topic_response,
                    "qos": 0,
                    "payload": payload_response,
                    "retain": False,
                },
            }
        ],
        "enable": True,
        "description": f"sensor:{sensor.unique_id}|{payload_response}",
        "metadata": {},
    }

    response_get_rule = requests.get(
        f"{EMQX_API_HOST}/rules/{rule_id}", headers=headers
    )

    if response_get_rule.status_code == 404:
        response = requests.post(
            f"{EMQX_API_HOST}/rules/", json=body, headers=headers
        )
    else:
        response = requests.put(
            f"{EMQX_API_HOST}/rules/{rule_id}", json=body, headers=headers
        )
    # response_json = response.json()
    return response


def delete_sensor_rule(sensor):
    """ delete sensor rule"""
    rule_id = f"sensor_{sensor.id}"
    EMQX_API_HOST = os.getenv("EMQX_API_HOST")
    AUTH_HEADER = (
        "Basic "
        + base64.b64encode(
            (
                os.getenv("EMQX_API_KEY") + ":" + os.getenv("EMQX_API_SECRET")
            ).encode()
        ).decode()
    )
    headers = {"Accept": "application/json", "Authorization": AUTH_HEADER}

    response_get_rule = requests.get(
        f"{EMQX_API_HOST}/rules/{rule_id}", headers=headers
    )
    if response_get_rule.status_code == 404:
        return response_get_rule.status_code
    response = requests.delete(f"{EMQX_API_HOST}/rules/{rule_id}", headers=headers)
    return response.status_code
