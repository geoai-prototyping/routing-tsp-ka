# Plan

## Compontents

0. Geocoder? --> Container/Free API? Address2Coords 
1. DB --> Save Addresses, Coords, Routes, Matrix(?) 
2. Routing --> Container OSRM / Valhalla
3. Dashboard --> Visulize DB Data: Points and Routes, some KPIs e.g. mean Traveltime, length
5. Conventional TSP --> 
4. TSP GeoAI --> Reasearch GeoAI

Region: Landkreis Karlsruhe

## Phase 1: Data Prep
Measure and save runtime via loggin (?)
1. https://download.geofabrik.de/europe/germany/baden-wuerttemberg/karlsruhe-regbez.html
2. Clip to Landkreis Karlsruhe in pbf format --> Routing Container
3. Address Data: Beverage markets as starting points, restaurants as delivery destinations (Scrape OR directly from OSM?)
4. Save data as geojson

## Phase 2: Data Visualization
1. 
