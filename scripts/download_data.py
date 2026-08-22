from routing_tsp_ka.data.download import download_data

# Direct test parameters
KAGEOFABRIK_URL = "https://download.geofabrik.de/europe/germany/baden-wuerttemberg/karlsruhe-regbez-latest.osm.pbf"
KAGEOFABRIK_OUTPUT = "data/raw/karlsruhe-regbez-latest.osm.pbf"

#LGLKALK_URL = "https://metadaten.geoportal-bw.de/geonetwork/srv/api/records/10f3233b-e83f-89ac-bfda-caa58e69ce9c?language=all"
#LGLKALK_OUTPUT = "data/raw/landkreis_ka_poly.geojson"

def main() -> None:
    """Test download function."""
    print(f"Starting test download from:\n  {KAGEOFABRIK_URL}")
    print(f"Saving to:\n  {KAGEOFABRIK_OUTPUT}\n")

    download_data(url=KAGEOFABRIK_URL, output_path=KAGEOFABRIK_OUTPUT)

    #download_data(url=LGLKALK_URL, output_path=LGLKALK_OUTPUT)



if __name__ == "__main__":
    main()