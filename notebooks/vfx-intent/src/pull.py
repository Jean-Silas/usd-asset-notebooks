import urllib
import urllib.request
import os
import sys

import pathlib

root = pathlib.Path(__file__).parent.parent.parent.parent

def teapot():
    url = "https://raw.githubusercontent.com/usd-wg/assets/refs/heads/main/full_assets/Teapot/geo/UtahTeapot.usd"
    save_to = root / 'assets' / 'UtahTeapot.usd'
    print(save_to)
    file = urllib.request.urlretrieve(
        url,
        filename=save_to
    )