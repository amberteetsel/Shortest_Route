from modules.graph import Graph
from modules.mapGraph import build_graph_from_json
import folium
from IPython.display import display
import random
import numpy as np

# Build graph & mappings
def build_graph_mappings(data, start, end, scenario, uncertainty):

    g, id_map, index_to_node_id = build_graph_from_json(data, scenario, uncertainty)

    path_indices = g.get_path(start, end)

    # print("Shortest path indices:", path_indices)
    print("Shortest path names:", [g.vertex_data[i] for i in path_indices])

    # Folium visualization
    m = folium.Map(location=[40.75, -73.98], zoom_start=13, tiles='CartoDB Positron')

    def get_latlon(node_index):
        node_id = index_to_node_id[node_index]
        node = data["nodes"][node_id]
        return node["lat"], node["lon"]
    
    # Collect all shortest path edges as a set of tuples for easy lookup
    shortest_path_edges = set()
    for i in range(len(path_indices) - 1):
        u = path_indices[i]
        v = path_indices[i + 1]
        shortest_path_edges.add(tuple(sorted((u, v))))

    # Draw all edges (blue) with labels (in minutes), except those in shortest path
    drawn_edges = set()
    for u in range(g.size):
        for v in range(g.size):
            if g.adj_matrix[u][v] != 0:
                edge_key = tuple(sorted((u, v)))
                if edge_key not in drawn_edges:
                    # Skip drawing blue label if edge is in shortest path edges
                    if edge_key not in shortest_path_edges:
                        loc_from = get_latlon(u)
                        loc_to = get_latlon(v)
                        time_val = g.adj_matrix[u][v]
    
                        folium.PolyLine(
                            locations=[loc_from, loc_to],
                            color='blue',
                            weight=2,
                            opacity=0.5
                        ).add_to(m)
    
                        mid_lat = (loc_from[0] + loc_to[0]) / 2
                        mid_lon = (loc_from[1] + loc_to[1]) / 2
                        folium.map.Marker(
                            [mid_lat, mid_lon],
                            icon=folium.DivIcon(html=f"""
                                <div style="font-size: 9px; color: blue;
                                            background-color: rgba(255,255,255,0.7);
                                            padding: 2px 4px; border-radius: 3px;
                                            border: 1px solid blue;
                                            white-space: nowrap;">
                                    {time_val:.2f} min
                                </div>
                            """)
                        ).add_to(m)
    
                    drawn_edges.add(edge_key)

    
    # Highlight shortest path edges (red) with thicker line and labels (in minutes)
    for i in range(len(path_indices) - 1):
        u = path_indices[i]
        v = path_indices[i + 1]
        loc_from = get_latlon(u)
        loc_to = get_latlon(v)
        time_val = g.adj_matrix[u][v]
    
        folium.PolyLine(
            locations=[loc_from, loc_to],
            color='red',
            weight=5,
            opacity=0.8
        ).add_to(m)
    
        mid_lat = (loc_from[0] + loc_to[0]) / 2
        mid_lon = (loc_from[1] + loc_to[1]) / 2
        folium.map.Marker(
            [mid_lat, mid_lon],
            icon=folium.DivIcon(html=f"""
                <div style="font-size: 10px; color: red;
                            background-color: rgba(255,255,255,0.9);
                            padding: 3px 5px; border-radius: 4px;
                            border: 1px solid red;
                            font-weight: bold; white-space: nowrap;">
                    {time_val:.2f} min
                </div>
            """)
        ).add_to(m)
        
    # Draw nodes with labels, highlighting shortest path nodes in red
    for idx in range(g.size):
        lat, lon = get_latlon(idx)
        color = 'red' if idx in path_indices else 'gray'
        
        # Larger circle marker for better visibility
        folium.CircleMarker(
            location=[lat, lon],
            radius=8,
            color=color,
            fill=True,
            fill_color=color,
            fill_opacity=0.9,
            weight=2,
            popup=g.vertex_data[idx],
            tooltip=g.vertex_data[idx]
        ).add_to(m)
        
        # Persistent label next to the node
        folium.map.Marker(
            [lat, lon],
            icon=folium.DivIcon(html=f"""
                <div style="font-size: 12px; font-weight: bold; 
                            color: {color}; 
                            background-color: rgba(255,255,255,0.7); 
                            padding: 2px 4px; border-radius: 3px;
                            white-space: nowrap;
                            border: 1px solid {color};
                            ">
                    {g.vertex_data[idx]}
                </div>
            """)
        ).add_to(m)
    
    # Legend update
    legend_html = '''
    <div style="
        position: fixed; 
        bottom: 50px; left: 50px; width: 210px; height: 110px; 
        background-color: white; 
        border:2px solid grey; 
        z-index:9999; 
        font-size:14px; 
        padding: 10px;
        box-shadow: 3px 3px 6px rgba(0,0,0,0.2);
        ">
        <b>Legend</b><br>
        <span style="color:red;">●</span> Shortest Path Node<br>
        <span style="color:gray;">●</span> Other Nodes<br>
        <span style="color:red;">━</span> Shortest Path Edge (time in minutes)<br>
        <span style="color:blue;">━</span> Other Edges (time in minutes)<br>
    </div>
    '''
    m.get_root().html.add_child(folium.Element(legend_html))
    
    # Show map inline
    display(m)