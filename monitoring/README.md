# 📊 Monitoring: Observability and Operations

This directory contains the operational dashboards and observability configurations for the **Aero-Climate Engineering** project.

## Observability

### 1. Prometheus
- **Metrics**: Flight telemetry, sensor data, model inference latency.
- **Scrape Jobs**: Data ingestion from edge devices.

### 2. Grafana
- **Dashboards**: Real-time atmospheric profile and seeding effectiveness analysis.
- **Alerting**: System health and safety limit breach notifications.

## Stack
- **Ingress**: NGINX / Cloudflare Warp.
- **Storage**: InfluxDB (Time-series data).
- **Visualization**: Grafana with custom dashboard templates.
