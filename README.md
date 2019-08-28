# Census Centroids
A collection of CSV files with the latitude/longitude for the centroid of each census shape. These are useful for making dot maps, or other maps where you might need to plot a single discrete location for a given shape.

Available files include:
* US counties (counties.csv)
* Census Places (places.csv)
* Census Tracts (tracts.csv)
* Zip Code Tabulation Areas (zctas.csv)

It doesn't include census blocks by default, since it would create a prohibitively large file. It should theoretically work using `make blocks.csv`, so feel free to give it a try if you've got the hardware and internet connection to spare. (It might take a few hours.) 

All the shapefiles come from the Census Bureau's TIGER database, using [@datadesk](https://github.com/datadesk)'s [census-map-downloader](https://github.com/datadesk/census-map-downloader) tool.

## Installation
If you want to generate files yourself, you'll first need to install [pipenv](https://pipenv.readthedocs.io/en/latest/). If you're on a mac, that's as easy as:
```
$ brew install pipenv
```

Then, you need to install the python dependencies:
```
$ pipenv install
```

## Usage
To generate files, just use the makefile commands:
```
$ make [format].csv
```
Where format is one of `counties`, `places`, `tracts`, `zctas`, or `blocks`. Or, you can run
```
$ make all
```
to generate every format (except for blocks, which is disabled by default).