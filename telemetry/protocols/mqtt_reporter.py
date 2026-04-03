import paho.mqtt.client as mqtt
import json
import time
import random

# Configuration
BROKER_URL = "telemetry.aero-climate.org"
BROKER_PORT = 1883
TOPIC_TELEMETRY = "aero/telemetry/drone-alpha"
TOPIC_COMMAND = "aero/commands/drone-alpha"

class AeroTelemetryClient:
    """
    Robust MQTT-based telemetry reporter for Aero-Climate Engineering drones.
    Handles atmospheric data transmission and incoming command subscriptions.
    """
    def __init__(self, client_id="DRONE_ALFA_01"):
        self.client_id = client_id
        self.client = mqtt.Client(client_id=self.client_id)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        print(f"[INFO] Initializing Telemetry Client: {self.client_id}")

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print(f"[CON] Connected to Telemetry Broker: {BROKER_URL}")
            self.client.subscribe(TOPIC_COMMAND)
            print(f"[SUB] Subscribed to topic: {TOPIC_COMMAND}")
        else:
            print(f"[ERR] Connection failed. Code: {rc}")

    def on_message(self, client, userdata, msg):
        payload = msg.payload.decode()
        print(f"[CMD] Command Received: {msg.topic} -> {payload}")
        try:
            cmd_data = json.loads(payload)
            if cmd_data.get("action") == "START_SEEDING":
                print("[ACT] EXECUTING SEEDING PAYLOAD RELEASE...")
            elif cmd_data.get("action") == "STOP_SEEDING":
                print("[ACT] STOPPING SEEDING OPERATIONS.")
        except json.JSONDecodeError:
            print("[ERR] Invalid command format.")

    def publish_telemetry(self, data):
        """Prepare and send atmospheric data to the command center."""
        payload = json.dumps({
            "client_id": self.client_id,
            "data": data,
            "ts": time.time()
        })
        self.client.publish(TOPIC_TELEMETRY, payload, qos=1)
        print(f"[PUB] Telemetry Sent to: {TOPIC_TELEMETRY}")

    def start(self):
        print("[CONN] Attempting connection to Broker...")
        # self.client.connect(BROKER_URL, BROKER_PORT, 60)
        # self.client.loop_start()

if __name__ == "__main__":
    reporter = AeroTelemetryClient()
    reporter.start()
    
    # Mock telemetry loop
    try:
        while True:
            # Simulate atmospheric data collection
            mock_data = {
                "alt_m": 2500 + random.uniform(-10, 10),
                "temp_c": -5.2 + random.uniform(-0.5, 0.5),
                "humi_pct": 88.5 + random.uniform(-2, 2)
            }
            reporter.publish_telemetry(mock_data)
            time.sleep(5)
    except KeyboardInterrupt:
        print("\n[INFO] Telemetry Client Stopped.")
        # reporter.client.loop_stop()
        # reporter.client.disconnect()
