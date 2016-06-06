import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    
    
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

def on_publish(client, userdata, mid):
    print("msg published " +str(mid))
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish


client.connect('192.168.1.27', 1883, 60)
client.publish("sensors/temperature", 88)
client.loop_start()
time.sleep(5)
client.loop_stop()

