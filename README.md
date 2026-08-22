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