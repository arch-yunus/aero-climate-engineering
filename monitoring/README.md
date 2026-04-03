# 📊 Monitoring: Observability and Operations

This directory contains the operational dashboards and observability configurations for the **Aero-Climate Engineering** project.

## Components & Files

### 1. [`docker-compose.yml`](./docker-compose.yml)
- **Services**: Prometheus, Grafana, InfluxDB.
- **Orchestration**: Single-command deployment for the entire monitoring stack.

### 2. [`prometheus.yml`](./prometheus.yml)
- **Scrape Jobs**: Pre-configured targets for telemetry and Edge AI vision modules.

## Stack
- **Ingress**: NGINX / Cloudflare Warp.
- **Storage**: InfluxDB (Time-series data).
- **Visualization**: Grafana with custom dashboard templates.
