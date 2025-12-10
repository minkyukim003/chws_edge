import paho.mqtt.client as mqtt
import json, time, inspect

EDGE_IP = "localhost"

def create_mqtt_client(name):
    sig = inspect.signature(mqtt.Client.__init__)
    if "callback_api_version" in sig.parameters:
        from paho.mqtt.client import CallbackAPIVersion
        return mqtt.Client(
            client_id=name,
            protocol=mqtt.MQTTv311,
            callback_api_version=CallbackAPIVersion.VERSION2
        )
    else:
        return mqtt.Client(client_id=name, protocol=mqtt.MQTTv311)


def on_message(client, userdata, msg):
    print(f"[EDGE] Forwarding: {msg.topic}")
    global running

    if msg.topic == "experiment/start":
        client.publish("vehicleB/start", msg.payload)

    elif msg.topic == "hazard/chws":
        client.publish("vehicleB/hazard", msg.payload)

    elif msg.topic == "experiment/end":
        print("[EDGE] Relaying shutdown.")
        client.publish("experiment/end", msg.payload)
        client.disconnect()
        raise SystemExit
    
    elif msg.topic == "warmup/ping":
        client.publish("warmup/pong", msg.payload)


def main():
    client = create_mqtt_client("EdgeServer")
    client.connect(EDGE_IP, 1883)

    client.subscribe("warmup/ping")

    client.subscribe("experiment/start")
    client.subscribe("hazard/chws")
    client.subscribe("experiment/end")
    
    client.on_message = on_message

    print("[EDGE] Running...")
    client.loop_forever()


if __name__ == "__main__":
    try:
        main()
    
    except KeyboardInterrupt:
        print("\n[EDGE] Shutting down...")
        time.sleep(1)
