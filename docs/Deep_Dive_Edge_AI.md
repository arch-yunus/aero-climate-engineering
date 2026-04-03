# 🧠 Deep Dive: Edge AI and Computer Vision in Climate Engineering

This document outlines the machine learning architecture and computer vision algorithms for the **Aero-Climate Engineering** project.

## 1. Cloud Masking and Macro-Morphology

The first task is to identify and segment the cloud structure from the atmosphere.

### Model Architecture:
- **ResNet18/34 Backbone**: Balanced for feature extraction and computational speed.
- **DeepLabV3+ Encoder-Decoder**: High-resolution segmentation for cloud edges.

### Feature Space:
- **Texture Gradients**: Identifying the difference between high-altitude cirrus (thin, ice-based) and cumulus towers (dense, water-based).
- **Spectral Ratios**: Analyzing pixel intensity in various light spectra to estimate water content ($W_c$).

---

## 2. Optimization for Edge Deployment (The "SBC" Bottleneck)

Small UAVs use **Single Board Computers (SBCs)** like NVIDIA Jetson Nano or Raspberry Pi 4/5. Running full-scale CNNs is impossible without significant optimization.

### Techniques Used:
1.  **Post-Training Quantization (PTQ)**: Converting FP32 weights to **INT8**. Over $4\times$ reduction in model size and inference latency.
    - Loss in accuracy is minimal ($< 1.5\%$) while throughput increases significantly.
2.  **Structural Pruning**: Removing redundant neurons that contribute least to the final decision.
3.  **ONNX Runtime / TensorRT Acceleration**: Using graph optimizations and layer fusion to maximize GPU/NPU utilization.

---

## 3. Probabilistic Decision-Making (Trigger Logic)

Aero-Climate Engineering does not use binary "Seed / No-Seed" logic. Instead, we use a **Probabilistic Inference Model**.

### Variables in the Decision Vector ($ \mathbf{v} $):
- $ p(\text{cloud\_type} = \text{Cumulus}) $: Vision-based probability.
- $ H_{rel} > 80\% $: Relative humidity from sensor fusion.
- $ T < 0^\circ C $: Temperature threshold.
- $ w_{\uparrow} > 2\text{m/s} $: Updraft velocity measurement.

The triggering function ($ f_{seed} $) initiates the payload release when:
$$ \mathcal{P}_{total} = \omega_1 p_{vision} + \omega_2 p_{sensors} > \Gamma_{threshold} $$
Where $ \omega $ are weighting factors optimized for various climatic regions (e.g., Arid vs. Tropical).

---

## 4. Dataset and Training

- **Data Sources**: EUMETSAT satellite data, ground-based time-lapse photography, and high-altitude ИHА flight footage.
- **Labeling**: "Precipitation-ready" vs. "Inactive" cloud labels, validated against historical rainfall data.

---
> [!TIP]
> The primary challenge in Edge AI is dealing with **glare and over-exposure** at high altitudes. All our vision scripts include automated exposure normalization (histogram equalization) before inference.
