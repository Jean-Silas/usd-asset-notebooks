# USD Asset Notebooks

A quick and dirty example of how you can break down a USD asset workflow into a Jupyter notebook, set up in a way where the USD assets are pulled in remotely.

The asset pulling is currently very rudimentary; we're just hitting `https://raw.githubusercontent.com/usd-wg/assets/refs/heads/main/*` to grab existing assets from [usd-wg/assets](https://github.com/usd-wg/assets). It will likely be adjusted to pull from object storage in a future commit.