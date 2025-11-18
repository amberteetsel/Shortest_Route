from src.modules.graph import Graph
import json


with open('manhattan_driving_distances.json', 'r') as f:
    loaded_dict = json.load(f)

# average traffic time
g = Graph(len(loaded_dict['nodes']))

for key in loaded_dict['nodes'].keys():
    g.add_vertex_data(int(key), loaded_dict['nodes'][key]["name"])

for i in loaded_dict["pairwise"].keys():
    for j in loaded_dict["pairwise"][i].keys():
        g.add_edge(int(i), int(j), loaded_dict["pairwise"][i][j]['avg_time_min'])

distances = g.dijkstra("Times Square")
for i, d in enumerate(distances):
    print(f"Distance from Times Square to {g.vertex_data[i]} during average traffic hours: {d}")
distances = g.dijkstra("Rockefeller Center")
for i, d in enumerate(distances):
    print(f"Distance from Empire State Building to {g.vertex_data[i]} during average traffic hours: {d}")
distances = g.dijkstra("Empire State Building")
for i, d in enumerate(distances):
    print(f"Distance from 'Union Square ' to {g.vertex_data[i]} during average traffic hours : {d}")

# peak traffic time
g = Graph(len(loaded_dict['nodes']))

for key in loaded_dict['nodes'].keys():
    g.add_vertex_data(int(key), loaded_dict['nodes'][key]["name"])

for i in loaded_dict["pairwise"].keys():
    for j in loaded_dict["pairwise"][i].keys():
        g.add_edge(int(i), int(j), loaded_dict["pairwise"][i][j]['peak_time_min'])

distances = g.dijkstra("Times Square")
for i, d in enumerate(distances):
    print(f"Distance from Times Square to {g.vertex_data[i]} during peak traffic hours: {d}")
distances = g.dijkstra("Rockefeller Center")
for i, d in enumerate(distances):
    print(f"Distance from Empire State Building to {g.vertex_data[i]} during peak traffic hours: {d}")
distances = g.dijkstra("Empire State Building")
for i, d in enumerate(distances):
    print(f"Distance from 'Union Square ' to {g.vertex_data[i]} during peak traffic hours : {d}")

