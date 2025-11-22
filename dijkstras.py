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
    print(f"Distance from Rockefeller Center to {g.vertex_data[i]} during average traffic hours: {d}")
distances = g.dijkstra("Empire State Building")
for i, d in enumerate(distances):
    print(f"Distance from Empire State Building to {g.vertex_data[i]} during average traffic hours : {d}")

for i in g.adj_matrix:
    for j in i:
        print(j, '\t', end= '')
    print()
print()
for i in g.adj_matrix:
    for j in i:
        print(j, '\t', end= '')
    print()

# Simulated peak traffic times
g_sim_peak_traffic = Graph(len(loaded_dict['nodes']))
for key in loaded_dict['nodes'].keys():
    g_sim_peak_traffic.add_vertex_data(int(key), loaded_dict['nodes'][key]["name"])

mean = 2
std = 0.5
for i in loaded_dict["pairwise"].keys():
    for j in loaded_dict["pairwise"][i].keys():
        g_sim_peak_traffic.add_edge(int(i), int(j), loaded_dict["pairwise"][i][j]['avg_time_min']*np.random.normal(mean, std))

distances = g_sim_peak_traffic.dijkstra("Times Square")
for i, d in enumerate(distances):
    print(f"Distance from Times Square to {g_sim_peak_traffic.vertex_data[i]} during simulated peak traffic hours: {d}")
distances = g_sim_peak_traffic.dijkstra("Rockefeller Center")
for i, d in enumerate(distances):
    print(f"Distance from Rockefeller Center to {g_sim_peak_traffic.vertex_data[i]} during simulated peak traffic hours: {d}")
distances = g_sim_peak_traffic.dijkstra("Empire State Building")
for i, d in enumerate(distances):
    print(f"Distance from Empire State Building to {g_sim_peak_traffic.vertex_data[i]} during simulated peak traffic hours : {d}")

# peak traffic time
g_peak_traffic = Graph(len(loaded_dict['nodes']))
for key in loaded_dict['nodes'].keys():
    g_peak_traffic.add_vertex_data(int(key), loaded_dict['nodes'][key]["name"])

for key in loaded_dict['nodes'].keys():
    g_peak_traffic.add_vertex_data(int(key), loaded_dict['nodes'][key]["name"])

for i in loaded_dict["pairwise"].keys():
    for j in loaded_dict["pairwise"][i].keys():
        g_peak_traffic.add_edge(int(i), int(j), loaded_dict["pairwise"][i][j]['peak_time_min'])

distances = g_peak_traffic.dijkstra("Times Square")
for i, d in enumerate(distances):
    print(f"Distance from Times Square to {g_peak_traffic.vertex_data[i]} during peak traffic hours: {d}")
distances = g_peak_traffic.dijkstra("Rockefeller Center")
for i, d in enumerate(distances):
    print(f"Distance from Rockefeller Center to {g_peak_traffic.vertex_data[i]} during peak traffic hours: {d}")
distances = g_peak_traffic.dijkstra("Empire State Building")
for i, d in enumerate(distances):
    print(f"Distance from Empire State Building to {g_peak_traffic.vertex_data[i]} during peak traffic hours : {d}")

# Simulated disruptions in traffic
g_sim_disruptions = Graph(len(loaded_dict['nodes']))
for key in loaded_dict['nodes'].keys():
    g_sim_disruptions.add_vertex_data(int(key), loaded_dict['nodes'][key]["name"])

for i in loaded_dict["pairwise"].keys():
    for j in loaded_dict["pairwise"][i].keys():
        rand_val = random.random() 
        if rand_val < 0.8:
            # No disruption
            g_sim_disruptions.add_edge(int(i), int(j), loaded_dict["pairwise"][i][j]['avg_time_min'])
        else:
            # Add disruption
            rand_val2 = random.random()
            if rand_val2 <= 0.5:
                # By making weight for the edge 0
                g_sim_disruptions.add_edge(int(i), int(j), float('inf'))
            else:
                # By making weight for the edge weight 10x
                g_sim_disruptions.add_edge(int(i), int(j), loaded_dict["pairwise"][i][j]['avg_time_min']*10)
                

# g_sim_disruptions.simulate_traffic()
distances = g_sim_disruptions.dijkstra("Times Square")
for i, d in enumerate(distances):
    print(f"Distance from Times Square to {g_sim_disruptions.vertex_data[i]} with simulated disruption in traffic hours: {d}")
distances = g_sim_disruptions.dijkstra("Rockefeller Center")
for i, d in enumerate(distances):
    print(f"Distance from Rockefeller Center to {g_sim_disruptions.vertex_data[i]} with simulated disruption in traffic hours: {d}")
distances = g_sim_disruptions.dijkstra("Empire State Building")
for i, d in enumerate(distances):
    print(f"Distance from Empire State Building to {g_sim_disruptions.vertex_data[i]} with simulated disruption in traffic hours : {d}")
