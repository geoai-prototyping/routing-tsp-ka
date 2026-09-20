COMPOSE_FILE := docker/routing/docker-compose.yml
PORT := 6000

.PHONY: up init chmod single-route nxn-matrix clean

up:
	docker compose -f $(COMPOSE_FILE) up -d osrm-routing

init:
	docker compose -f $(COMPOSE_FILE) --profile init up

single-route:
	curl -s "http://localhost:$(PORT)/route/v1/driving/8.48608,49.00838;8.49108,49.00338?overview=false"

matrix:
	uv run scripts/test_osrm.py

clean:
	docker compose -f $(COMPOSE_FILE) down --volumes