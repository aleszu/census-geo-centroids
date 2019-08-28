import argparse
import sys
import csv
import geopandas as gpd 

parser = argparse.ArgumentParser(description="Calculates centroids of GeoJSON Features and writes the results to a file")
parser.add_argument('geojson', type=str, help="GeoJSON file to read features from")
parser.add_argument('-o', '--out', help="File to write output to")

args = parser.parse_args()

outfile = sys.stdout
if args.out:
  try:
    outfile = open(args.out, 'w')
  except Exception as e:
    print(f"Error: Could not open output file {args.out}", file=sys.stderr)
    sys.exit(1)

csvwriter = csv.DictWriter(outfile, fieldnames=['geoid', 'latitude', 'longitude'])
csvwriter.writeheader()

geos = gpd.read_file(args.geojson)
geos['centroid'] = geos.centroid

for index, row in geos.iterrows():
  csvwriter.writerow({
    'geoid': getattr(row, 'geoid', getattr(row, 'GEOID', getattr(row, 'GeoId', None))),
    'longitude': row.centroid.x,
    'latitude': row.centroid.y
  })

outfile.close()

