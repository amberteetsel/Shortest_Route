from gmplot import gmplot

loc_dict = {
'Times Square (Broadway & 7th Ave)': (40.7570, -73.98597 ),
'Rockefeller Center (45 Rockefeller Plaza)': (40.75926, -73.97996 ),
'Bryant Park / New York Public Library (42nd St & 6th Ave)': (40.75361, -73.98417 ),
'Grand Central Terminal (89 E 42nd St)': (40.75273, -73.97723 ),
'Empire State Building (350 5th Ave)': (40.74844, -73.98566),
'Flatiron Building / Madison Square Park (23rd St & 5th Ave)': (40.74103, -73.98969 ),
'Union Square (14th St & Broadway)': (40.7367, -73.9899 ),
'Chelsea / Chelsea Market (15th St / High Line access near Gansevoort)': (40.7388, -74.0037 ),
'Washington Square Park (W 4th St, Greenwich Village)': (40.73082, -73.99733 ),
'Battery Park / South Ferry (southern tip of Manhattan)': (40.70314, -74.01600 )
}

gmap = gmplot.GoogleMapPlotter(40.7570, -73.98597, 13)

for key in loc_dict.keys():
    print(key, loc_dict[key][0], loc_dict[key][1])
    gmap.marker(loc_dict[key][0], loc_dict[key][1], 'cornflowerblue', title = key)

gmap.draw("my_map.html")

