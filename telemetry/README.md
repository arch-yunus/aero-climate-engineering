# 📡 Telemetry: Communication Protocols

This directory contains the telecommunication and data handling protocols for the **Aero-Climate Engineering** project.

## Components & Files

### 1. [`protocols/mqtt_reporter.py`](./protocols/mqtt_reporter.py)
- **Protocol**: MQTT.
- **Function**: Robust ground-to-air telemetry and command uplink/downlink.
- **Security**: Supports TLS/SSL for secure atmospheric operations.

## Hardware Support
- **Comms**: LoRaWAN (Long Range Wide Area Network) / Sub-GHz RF.
- **Redundancy**: Dual-link communication with satellite backup (optional).
