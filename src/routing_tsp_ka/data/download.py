import urllib.request
from pathlib import Path

from loguru import logger
from tqdm import tqdm

logger = logger.opt(depth=2)


def download_data(url: str, output_path: str) -> None:
    """Downloads data from a url to a path.

    input:
        url: str
        output_path: str
    output:
        None
    """
    target = Path(output_path)
    target.parent.mkdir(parents=True, exist_ok=True)

    logger.info(f"Downloading data from {url} to {output_path}")

    # Get the size of the file
    with urllib.request.urlopen(url) as response:
        total_size = int(response.headers.get('content-length', 0))

    # Combine the with statements
    with urllib.request.urlopen(url) as link, target.open("wb") as out_file, tqdm(total=total_size, unit='B', unit_scale=True, unit_divisor=1024) as bar:
        for data in iter(lambda: link.read(4096), b''):
            out_file.write(data)
            bar.update(len(data))
