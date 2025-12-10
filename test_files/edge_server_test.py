import paho.mqtt.client as mqtt
from paho.mqtt.client import CallbackAPIVersion

def on_message(client, userdata, msg):
    print(f"[EDGE] Received from {msg.topic}: {msg.payload.decode()}")
    client.publish("hazard/global", msg.payload)

client = mqtt.Client(
    client_id="EdgeServer",
    callback_api_version=CallbackAPIVersion.VERSION2
)

client.connect("localhost", 1883)
client.subscribe("vehicle/+/hazard")
client.on_message = on_message

try:
    print("[EDGE] Running…")
    client.loop_forever()

except KeyboardInterrupt:
    print("Disconnected edge server. Not receiving or sending hazard information.")

#Receive from A and send to B