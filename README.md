> **Status:** Setup & Data Preparation Phase

A benchmark platform comparing **Conventional TSP Solvers** (OR-Tools, heuristics) against **GeoAI Approaches** for regional beverage-to-restaurant delivery logistics in **Landkreis Karlsruhe**.

---

## Project Structure

```text
routing-tsp-ka/
├── .github/workflows/    # CI (Ruff linting & formatting)
├── data/                 # Raw/Processed OSM data & routing graphs (git-ignored)
│   ├── raw/              # Downloaded Geofabrik extracts (.pbf)
│   ├── processed/        # Clipped PBFs & target GeoJSON files
│   └── routing/          # OSRM / Valhalla graph files
├── docker/               # Container configs
│   ├── dashboard/        # UI Dockerfile
│   └── routing/          # OSRM preprocessing scripts
├── notebooks/            # EDA & spatial prototyping
├── src/routing_tsp_ka/   # Core Python package
│   ├── data/             # OSM downloading, clipping, geocoding, scraping
│   ├── routing/          # OSRM / Valhalla matrix API clients
│   ├── solvers/          # Conventional & GeoAI TSP solvers
│   ├── dashboard/        # Streamlit web UI
│   └── utils/            # Logging timers & GeoJSON I/O
├── tests/                # Pytest test suite
├── docker-compose.yml    # Multi-container orchestration (Routing + UI)
├── pyproject.toml        # Project configuration & dependencies
└── uv.lock               # Deterministic dependency lockfile
```



---

## OSRM ROUTING

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

