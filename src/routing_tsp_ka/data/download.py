import shutil
import urllib.request
from pathlib import Path


def download_data(
        url: str, 
        output_path: str ) -> None:
    """Downloads data from an url to a path.

    input:
        url: str
        path: str
    output
        None
    """
    target = Path(output_path)
    target.parent.mkdir(parents=True, exist_ok=True)

    with urllib.request.urlopen(url) as link, target.open('wb') as out_file:
        shutil.copyfileobj(link, out_file)
