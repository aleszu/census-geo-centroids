import geopandas as gpd
import argparse

parser = argparse.ArgumentParser(description="Merge multiple geojson files into one file")
parser.add_argument('files', metavar='file', type=str, nargs='+', help="Files you want to merge")
parser.add_argument('-o', '--out', help="Output file to write to")
args = parser.parse_args()

df = gpd.pd.concat([ gpd.read_file(file) for file in args.files ])

df.to_file(args.out, driver="GeoJSON")