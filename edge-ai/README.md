# 🧠 Edge AI: On-device Atmospheric Control

This directory contains the machine learning models and optimization scripts for the **Aero-Climate Engineering** project.

## Models & Scripts

### 1. [`cloud_vision/cloud_classifier.py`](./cloud_vision/cloud_classifier.py)
- **Architecture**: MobileNetV3 (Quantized for SBC).
- **Function**: Real-time cloud type detection (Cumulus, Stratus, Cirrus).
- **Output**: Seeding activation signal.

### 2. Targeting Algorithms
- **Optimization**: Calculating the optimal seeding point using sensor fusion and wind vector analysis.

## Development

- **Framework**: TensorFlow Lite / ONNX Runtime.
- **Hardware Target**: NVIDIA Jetson / Raspberry Pi with AI Accelerator.
