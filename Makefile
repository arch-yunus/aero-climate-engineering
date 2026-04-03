.PHONY: setup help lint start-monitoring stop-monitoring clean

help:
	@echo "Aero-Climate Engineering - Operational Makefile"
	@echo "Commands:"
	@echo "  setup            Install project-wide dependencies"
	@echo "  lint             Check Python scripts for errors"
	@echo "  start-monitoring Launch Prometheus, Grafana, and InfluxDB stack"
	@echo "  stop-monitoring  Stop the monitoring stack"
	@echo "  clean          Remove temporary files and caches"

setup:
	@echo "Setting up development environment..."
	pip install -r requirements.txt
	@echo "Environment Ready."

lint:
	@echo "Linting Edge AI and Telemetry modules..."
	flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics

start-monitoring:
	@echo "Orbiting Monitoring Stack..."
	cd monitoring && docker-compose up -d
	@echo "Access Grafana at http://localhost:3000 (Pass: aero_climate_2026)"

stop-monitoring:
	@echo "De-orbiting Monitoring Stack..."
	cd monitoring && docker-compose down

clean:
	@echo "Purging system caches..."
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	@echo "Workspace Clean."
