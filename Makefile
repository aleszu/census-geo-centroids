# Census geos, except for blocks because it's too big
GEOS = counties_2018 places_2018 tracts_2010 zctas_2018 # blocks_2018

.PHONY: all
all: $(addsuffix .csv, $(GEOS))

%.csv: shapefiles/processed/%.geojson 
	# TODO use python to calculate centroids of shapefiles

# Special case to merge zctas from separate states
shapefiles/processed/zctas_2018.geojson: shapefiles/processed/zctas_2018_al.geojson
	pipenv run python3 merge.py shapefiles/processed/zctas_2018_*.geojson -o $@

# General case for downloading geojson files
shapefiles/processed/%.geojson:
	mkdir -p shapefiles
	pipenv run censusmapdownloader --data-dir shapefiles $(firstword $(subst _, ,$*))
