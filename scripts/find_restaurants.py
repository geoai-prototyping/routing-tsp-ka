import osmium
import pandas as pd


class OSMHandler(osmium.SimpleHandler):
    """Process OSM data."""
    def __init__(self):
        """Initialise Handler."""
        super().__init__()
        self.restaurants = []

    def node(self, n):
        """Process a node element from the OSM data."""
        tags = dict(n.tags)

        if "restaurant" in tags.get("amenity", ""):
            self.restaurants.append(tags)


if __name__ == '__main__':
    print("Finding restaurants.")
    handler = OSMHandler()
    handler.apply_file("./data/raw/karlsruhe-regbez-latest.osm.pbf")

    restaurant_frame = pd.DataFrame(handler.restaurants)
    restaurant_frame.to_parquet("./data/processed/restaurants.parquet", index=False)
    print(f"Restaurants: {restaurant_frame.head(5)}")