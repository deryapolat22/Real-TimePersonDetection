import random

from paho.mqtt import client as mqtt_client
from datetime import date, datetime

today = date.today()

import pyrebase
from datetime import date

today = date.today()

config = {
      'apiKey': "AIzaSyA8ppa2_8a6Bt0eQSzOnBocDb_tBXWPP3U",
      'authDomain': "project-379be.firebaseapp.com",
      'databaseURL': "https://project-379be-default-rtdb.europe-west1.firebasedatabase.app",
      'projectId': "project-379be",
      'storageBucket': "project-379be.appspot.com",
      'messagingSenderId': "517107064834",
      'appId': "1:517107064834:web:02bc809366266ffec6871b",
      'measurementId': "G-F3EY8LMYB0"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()


broker = 'broker.emqx.io'
port = 1883
topic = "myTopic"
client_id = f'python-mqtt-{random.randint(0, 100)}'
username = 'emqx'
password = 'public'


def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port, 20)
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

        val = str(msg.payload, 'UTF-8')
        data = {"Veri": val+str(datetime.now())}
        db.child(today).push(data)

        with open('test.txt', 'a+') as f:
            f.write(str("Message received: " + msg.payload.decode() + str(datetime.now()) + "\n"))


    client.subscribe(topic)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()
