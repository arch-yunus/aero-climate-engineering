# 🛠️ Aero-Climate Engineering: Bill of Materials (BOM)

This document lists the recommended components for building a project-standard autonomous cloud seeding UAV and its associated ground station.

## 🚁 1. UAV Platform (Heavy Lift Quad/Octo)

| Component | specification | Quantity | Notes |
| :--- | :--- | :--- | :--- |
| **Frame** | Carbon Fiber 900mm+ Wheelbase | 1 | High stability for high-altitude wind. |
| **Motors** | 400KV - 600KV Brushless | 4-8 | Efficiency is key for long-duration flights. |
| **ESC** | 60A - 80A Opto | 4-8 | BLHeli_32 preferred. |
| **Propellers** | 18" - 22" Carbon Fiber | 1 Set | Balanced for high-altitude thin air. |
| **Flight Controller** | Cube Orange / Pixhawk 6C | 1 | ArduPilot/PX4 compatible. |
| **GPS/GNSS** | Hex Here3 / Dual GPS | 1-2 | High precision for targeting. |

## 🧪 2. Seeding Payload & Control

| Component | specification | Quantity | Notes |
| :--- | :--- | :--- | :--- |
| **Seeding Canister** | Aluminum Alloy / Heat Shielded | 2-4 | Modular release system. |
| **Release Actuator** | 25kg High-Torque Metal Servo | 2-4 | Reliable under mechanical stress. |
| **Trigger Controller** | STM32 / Arduino Nano | 1 | Interfaces with Edge AI. |
| **Payload Sensor** | Temperature & Status Feedback | 1 Set | Health monitoring of the seeding agent. |

## 🧠 3. Edge AI & Telemetry Stack

| Component | specification | Quantity | Notes |
| :--- | :--- | :--- | :--- |
| **SBC (Edge AI)** | NVIDIA Jetson Orin Nano / RPi 5 | 1 | Real-time cloud classification. |
| **Camera Module** | Global Shutter / Wide Angle | 1 | Atmospheric vision. |
| **Telemetry Radio** | 433MHz / 915MHz LoRa | 1 Pair | Long range ground-to-air link. |
| **LTE Module** | SIM7600 / Quectel EC25 | 1 | Backup 4G/5G data link. |

## 📶 4. Ground Station & Monitoring

| Component | specification | Quantity | Notes |
| :--- | :--- | :--- | :--- |
| **Base Station** | Panasonic Toughbook / High-Perf Hub | 1 | Monitoring dashboard (Prometheus/Grafana). |
| **Sensors** | BME280, Anemometer, Rain Gauge | 1 Set | Ground truth validation. |
| **Power Supply** | 12V/24V External Power Rack | 1 | Field operations power. |

---
> [!IMPORTANT]
> Always verify local regulations regarding UAV weights and geoengineering experiments before procuring hardware.
