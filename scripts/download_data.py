from routing_tsp_ka.data.download import download_data

# Direct test parameters
TEST_URL = "https://download.geofabrik.de/europe/germany/baden-wuerttemberg/karlsruhe-regbez-latest.osm.pbf"
TEST_OUTPUT = "data/raw/karlsruhe-regbez-latest.osm.pbf"


def main() -> None:
    """Test download function."""
    print(f"Starting test download from:\n  {TEST_URL}")
    print(f"Saving to:\n  {TEST_OUTPUT}\n")

    download_data(url=TEST_URL, output_path=TEST_OUTPUT)


if __name__ == "__main__":
    main()