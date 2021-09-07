import os
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print('conecting, waiting for data.....')
    client.subscribe(topic=os.environ.get('MQTT_BROKER_TOPIC'), qos=2)

def on_message(client, userdata, message):
    print("--------------------------")
    print('topic: ', message.topic)
    var = str(message.payload.decode('utf-8'))
    print('payload: ', message.payload )
    try:
        # CON STRING DUMPS AND LOADS
        data = json.dumps(var)
        data = json.loads(data)
        print(data)
    except Exception as e:
        print(e)
    print('qos: ', message.qos)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set(os.environ.get('MQTT_BROKER_USERNAME'), os.environ.get('MQTT_BROKER_PASSWORD'))
client.connect(host=os.environ.get('MQTT_BROKER_HOST'),port=int(os.environ.get('MQTT_BROKER_PORT')))
client.loop_start()


