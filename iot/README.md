# 📡 IoT: Sensors and Data Ingestion

This directory contains the sensor network architecture for the **Aero-Climate Engineering** project.

## Sensor Network

### 1. Ground Sensors
- **Weather Stations**: Localized environmental data for seeding validation.
- **Connectivity**: WiFi / LoRa.

### 2. Airborne Sensors
- **In-flight Metering**: Real-time atmospheric profile collection.
- **Data Format**: JSON/Protobuf for minimal overhead.

## Hardware Support
- **Microcontrollers**: ESP32 / Arduino / STM32.
- **Sensors**: BME280, DHT22, GPS Neo-M8N.
