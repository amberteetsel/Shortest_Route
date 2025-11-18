from src.modules.graph import Graph
import json


with open('locations.json', 'r') as f:
    loaded_dict = json.load(f)

g = Graph(len(loaded_dict))

i = 0
for key in loaded_dict.keys():
    g.add_vertex_data(i, key)
    i += 1

g.add_edge(0, 1, 9)
g.add_edge(0, 2, 3)
g.add_edge(0, 3, 3)
g.add_edge(1, 7, 2)
g.add_edge(2, 3, 2)
g.add_edge(2, 4, 6)
g.add_edge(2, 6, 2)
g.add_edge(3, 4, 3)
g.add_edge(6, 7, 1)
g.add_edge(6, 5, 3)


distances = g.dijkstra('Times Square (Broadway & 7th Ave)')
for i, d in enumerate(distances):
    print(f"Distance from Times Square (Broadway & 7th Ave) to {g.vertex_data[i]}: {d}")
distances = g.dijkstra('Empire State Building (350 5th Ave)')
for i, d in enumerate(distances):
    print(f"Distance from Empire State Building (350 5th Ave) to {g.vertex_data[i]}: {d}")
distances = g.dijkstra('Union Square (14th St & Broadway)')
for i, d in enumerate(distances):
    print(f"Distance from 'Union Square (14th St & Broadway)' to {g.vertex_data[i]}: {d}")

