from gmplot import gmplot
import json

with open('manhattan_driving_distances.json', 'r') as f:
    loc_dict = json.load(f)

gmap = gmplot.GoogleMapPlotter(40.7570, -73.98597, 13)

for key in loc_dict['nodes'].keys():
    print(key, loc_dict['nodes'][key]['name'], loc_dict['nodes'][key]['lat'], loc_dict['nodes'][key]['lon'])
    gmap.marker(loc_dict['nodes'][key]['lat'], loc_dict['nodes'][key]['lon'], 'cornflowerblue', title = loc_dict['nodes'][key]['name'])

gmap.draw("location_visualizer.html")

