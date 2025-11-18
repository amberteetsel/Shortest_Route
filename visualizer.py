from gmplot import gmplot
import json

with open('locations.json', 'r') as f:
    loc_dict = json.load(f)

gmap = gmplot.GoogleMapPlotter(40.7570, -73.98597, 13)

for key in loc_dict.keys():
    print(key, loc_dict[key][0], loc_dict[key][1])
    gmap.marker(loc_dict[key][0], loc_dict[key][1], 'cornflowerblue', title = key)

gmap.draw("location_visualizer.html")

