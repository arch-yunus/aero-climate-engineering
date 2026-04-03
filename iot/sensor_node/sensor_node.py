import time
import machine
import bme280 # Mock library for illustration
import network
import ujson

# Configuration
WIFI_SSID = "AeroClimate_Net"
WIFI_PASS = "CloudSeeding2026"
SERVER_URL = "http://monitoring.aero.local/data"

class AeroSensorNode:
    """
    MicroPython-based sensor node for Aero-Climate Engineering.
    Collects high-precision atmospheric data for ground/drone telemetry.
    """
    def __init__(self, node_id="NODE_01"):
        self.node_id = node_id
        # Pin definitions for ESP32/ESP8266
        self.i2c = machine.I2C(scl=machine.Pin(22), sda=machine.Pin(21))
        self.bme = None # bme280.BME280(i2c=self.i2c)
        print(f"[INIT] {self.node_id}: Initialized I2C and sensors.")

    def connect_wifi(self):
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        if not wlan.isconnected():
            print("[NET] Connecting to WiFi...")
            wlan.connect(WIFI_SSID, WIFI_PASS)
            while not wlan.isconnected():
                pass
        print(f"[NET] Connected. IP: {wlan.ifconfig()[0]}")

    def read_sensors(self):
        """Mock sensor reading logic."""
        # Replace with actual: self.bme.values
        temp = 18.5 + (machine.rng() % 100) / 10.0
        humi = 75.0 + (machine.rng() % 50) / 10.0
        pres = 1013.25 + (machine.rng() % 200) / 10.0
        
        return {
            "node_id": self.node_id,
            "temp_c": temp,
            "humi_pct": humi,
            "pres_hpa": pres,
            "timestamp": time.time()
        }

    def run(self, interval=5):
        print(f"[RUN] Starting {self.node_id} Data Collection Loop...")
        while True:
            data = self.read_sensors()
            payload = ujson.dumps(data)
            print(f"[DATA] {payload}")
            
            # Here: urequests.post(SERVER_URL, data=payload)
            
            time.sleep(interval)

if __name__ == "__main__":
    node = AeroSensorNode(node_id="DRONE_ALFA_SENS")
    # node.connect_wifi()
    node.run()
