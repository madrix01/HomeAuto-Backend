import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect('192.168.29.69', 1883, 60)
client.loop_start()
