from src.modules.graph import Graph

g = Graph(8)

g.add_vertex_data(0, 'Times Square (Broadway & 7th Ave)')
g.add_vertex_data(1, 'Rockefeller Center (45 Rockefeller Plaza)')
g.add_vertex_data(2, 'Bryant Park / New York Public Library (42nd St & 6th Ave)')
g.add_vertex_data(3, 'Grand Central Terminal (89 E 42nd St)')
g.add_vertex_data(4, 'Empire State Building (350 5th Ave)')
g.add_vertex_data(5, 'Flatiron Building / Madison Square Park (23rd St & 5th Ave)')
g.add_vertex_data(6, 'Union Square (14th St & Broadway)')
g.add_vertex_data(7, 'Chelsea / Chelsea Market (15th St / High Line access near Gansevoort)')
g.add_vertex_data(8, 'Washington Square Park (W 4th St, Greenwich Village)')
g.add_vertex_data(9, 'Battery Park / South Ferry (southern tip of Manhattan)')

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

