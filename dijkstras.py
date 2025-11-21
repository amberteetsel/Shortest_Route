from src.modules.graph import Graph
import json
import numpy as np
import random

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

# Simulated peak traffic times
mean = 2
std = 0.5
for i in loaded_dict["pairwise"].keys():
    for j in loaded_dict["pairwise"][i].keys():
        g.add_edge(int(i), int(j), loaded_dict["pairwise"][i][j]['avg_time_min']*np.random.normal(mean, std))

# g.simulate_traffic()
distances = g.dijkstra("Times Square")
for i, d in enumerate(distances):
    print(f"Distance from Times Square to {g.vertex_data[i]} during simulated peak traffic hours: {d}")
distances = g.dijkstra("Rockefeller Center")
for i, d in enumerate(distances):
    print(f"Distance from Empire State Building to {g.vertex_data[i]} during simulated peak traffic hours: {d}")
distances = g.dijkstra("Empire State Building")
for i, d in enumerate(distances):
    print(f"Distance from 'Union Square ' to {g.vertex_data[i]} during simulated peak traffic hours : {d}")

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

# Simulated disruptions in traffic
for i in loaded_dict["pairwise"].keys():
    for j in loaded_dict["pairwise"][i].keys():
        rand_val = random.random() 
        if rand_val < 0.8:
            # No disruption
            g.add_edge(int(i), int(j), loaded_dict["pairwise"][i][j]['avg_time_min'])
        else:
            # Add disruption
            rand_val2 = random.random()
            if rand_val2 <= 0.5:
                # By making weight for the edge 0
                g.add_edge(int(i), int(j), 0)
            else:
                # By making weight for the edge weight 10x
                g.add_edge(int(i), int(j), loaded_dict["pairwise"][i][j]['avg_time_min']*10)
                

# g.simulate_traffic()
distances = g.dijkstra("Times Square")
for i, d in enumerate(distances):
    print(f"Distance from Times Square to {g.vertex_data[i]} with simulated disruption in traffic hours: {d}")
distances = g.dijkstra("Rockefeller Center")
for i, d in enumerate(distances):
    print(f"Distance from Empire State Building to {g.vertex_data[i]} with simulated disruption in traffic hours: {d}")
distances = g.dijkstra("Empire State Building")
for i, d in enumerate(distances):
    print(f"Distance from 'Union Square ' to {g.vertex_data[i]} with simulated disruption in traffic hours : {d}")
