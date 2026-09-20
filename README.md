> **Status:** Setup & Data Preparation Phase

A benchmark platform comparing **Conventional TSP Solvers** (OR-Tools, heuristics) against **GeoAI Approaches** for regional beverage-to-restaurant delivery logistics in **Landkreis Karlsruhe**.

---

## Table of Contents

- [Project Structure](#project-structure)
- [OSRM Routing](#osrm-routing)
- [Makefile](#makefile)

---

## Project Structure

```text
routing-tsp-ka/
├── .github/workflows/    # CI (Ruff linting & formatting)
├── data/                 # Raw/Processed OSM data & routing graphs (git-ignored)
│   ├── osrm/             # OSRM extracted graph files
│   ├── processed/        # Clipped PBFs & target GeoJSON files
│   └── raw/              # Downloaded Geofabrik extracts (.pbf)
├── docker/               # Container configs
│   ├── dashboard/        # UI Dockerfile
│   └── routing/          # OSRM pre-processing & service setup
│       └── docker-compose.yml
├── notebooks/            # EDA & spatial prototyping
├── scripts/              # Validation & benchmark execution scripts
│   └── test_osrm.py      # OSRM Table API matrix verification script
├── src/routing_tsp_ka/   # Core Python package
│   ├── dashboard/        # Web application & frontend assets
│   │   └── app/
│   │       ├── static/   # Web assets (CSS, JS, OpenLayers, ol-ext)
│   │       └── templates/# HTML view templates
│   ├── data/             # OSM downloading, clipping, geocoding, scraping
│   ├── routing/          # OSRM / Valhalla matrix API clients
│   ├── solvers/          # Conventional & GeoAI TSP solvers
│   └── utils/            # Logging timers & GeoJSON I/O
├── tests/                # Pytest test suite
├── Makefile              # Central orchestration commands
├── pyproject.toml        # Project configuration & dependencies
└── uv.lock               # Deterministic dependency lockfile
```

---

## OSRM Routing

The compose configuration handles two distinct operational phases:

### Initialization Profile (`--profile init`)

Runs three sequential OSRM processing steps (`osrm-extract -> osrm-partition -> osrm-customize`) using the Multi-Level Dijkstra (MLD) algorithm. It processes the raw `.osm.pbf` file from `data/osrm/` and generates the optimized binary routing graph files.

### Routing Server (`osrm-routing`)

Launches a persistent `osrm-routed` HTTP server on port 6000, exposing fast matrix and routing API endpoints to your Python solvers and dashboard.

### Running the Setup

```bash
# 1. Pre-process the Karlsruhe OSM data (run once)
docker compose -f docker/routing/docker-compose.yml --profile init up

# 2. Launch the background OSRM routing server
docker compose -f docker/routing/docker-compose.yml up -d osrm-routing
```

### Quick API Verification

Verify that the routing engine is up and responding on port 6000:

```bash
curl -s "http://localhost:6000/route/v1/driving/8.401,49.000;8.404,49.013?overview=false"
```

This setup ensures that the OSRM engine is correctly pre-processed and is ready for use in your project

---
## Makefile

A root Makefile for quick checks

```
up:
	docker compose -f $(COMPOSE_FILE) up -d osrm-routing

init:
	docker compose -f $(COMPOSE_FILE) --profile init up

route-test:
	curl -s "http://localhost:$(PORT)/route/v1/driving/8.48608,49.00838;8.49108,49.00338?overview=false"

matrix-test:
	uv run scripts/test_osrm.py

clean:
	docker compose -f $(COMPOSE_FILE) down --volumes

```

### Usage

```
make init          # Build routing graph files
make up            # Start OSRM engine background container
make route-test    # Run point-to-point query verification
make matrix-test   # Run Python N x N matrix test script
```