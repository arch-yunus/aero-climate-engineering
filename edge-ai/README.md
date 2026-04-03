# 🧠 Edge AI: On-device Atmospheric Control

This directory contains the machine learning models and optimization scripts for the **Aero-Climate Engineering** project.

## Models

### 1. Cloud Classification
- **Type**: CNN-based architecture (MobileNetV3 backbone).
- **Function**: Real-time cloud type detection (Cumulus, Stratus, Cirrus).

### 2. Density Analysis
- **Function**: Estimating water droplet density and potential for precipitation.

### 3. Targeting Algorithms
- **Optimization**: Calculating the optimal seeding point using sensor fusion and wind vector analysis.

## Development

- **Framework**: TensorFlow Lite / ONNX Runtime.
- **Hardware Target**: NVIDIA Jetson / Raspberry Pi with AI Accelerator.
