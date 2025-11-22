import json
import folium
from folium import plugins

with open('manhattan_driving_distances.json', 'r') as f:
    graph_data = json.load(f)

m = folium.Map(
    location=[40.7425, -73.9875],
    zoom_start=13,
    tiles='OpenStreetMap'
)

drawn_edges = set()

for from_id, connections in graph_data["pairwise"].items():
    from_node = graph_data["nodes"][from_id]
    
    for to_id, edge_data in connections.items():
        edge_key = tuple(sorted([from_id, to_id]))
        
        if edge_key not in drawn_edges:
            to_node = graph_data["nodes"][to_id]
            
            distance = edge_data.get("avg_distance_km", 0)
            avg_time = edge_data.get("avg_time_min", 0)
            peak_time = edge_data.get("peak_time_min", 0)
            
            mid_lat = (from_node["lat"] + to_node["lat"]) / 2
            mid_lon = (from_node["lon"] + to_node["lon"]) / 2
            
            edge_tooltip = f"""
            {from_node['name']} ↔ {to_node['name']}<br>
            Distance: {distance} km<br>
            Avg Time: {avg_time} min<br>
            Peak Time: {peak_time} min
            """
            
            folium.PolyLine(
                locations=[
                    [from_node["lat"], from_node["lon"]],
                    [to_node["lat"], to_node["lon"]]
                ],
                color='blue',
                weight=3,
                opacity=0.6,
                tooltip=edge_tooltip
            ).add_to(m)
            
            weight_label = f"{distance} km / {avg_time} min"
            folium.Marker(
                location=[mid_lat, mid_lon],
                icon=folium.DivIcon(html=f"""
                    <div style="font-size: 10px; color: #1a1a1a; 
                                background-color: rgba(255, 255, 255, 0.8); 
                                padding: 2px 4px; border-radius: 3px;
                                border: 1px solid #0066cc;
                                font-weight: bold; white-space: nowrap;">
                        {weight_label}
                    </div>
                """),
                tooltip=edge_tooltip
            ).add_to(m)
            
            drawn_edges.add(edge_key)

for node_id, node_data in graph_data["nodes"].items():
    connections_count = len(graph_data["pairwise"].get(node_id, {}))
    
    popup_text = f"""
    <b>{node_data['name']}</b><br>
    Node ID: {node_id}<br>
    Connections: {connections_count}<br>
    Lat: {node_data['lat']:.5f}<br>
    Lon: {node_data['lon']:.5f}
    """
    
    folium.Marker(
        location=[node_data["lat"], node_data["lon"]],
        popup=folium.Popup(popup_text, max_width=250),
        tooltip=node_data["name"],
        icon=folium.Icon(color='red', icon='info-sign')
    ).add_to(m)
    
    folium.CircleMarker(
        location=[node_data["lat"], node_data["lon"]],
        radius=8,
        color='darkred',
        fill=True,
        fillColor='red',
        fillOpacity=0.7,
        weight=2
    ).add_to(m)

legend_html = '''
<div style="position: fixed; 
            bottom: 50px; right: 50px; width: 200px; height: 120px; 
            background-color: white; border:2px solid grey; z-index:9999; 
            font-size:14px; padding: 10px">
<p><b>NYC Landmarks Graph</b></p>
<p><span style="color:red;">●</span> Landmark Node</p>
<p><span style="color:blue;">━</span> Direct Connection</p>
<p>Total Nodes: 10<br>Total Edges: 13</p>
</div>
'''
m.get_root().html.add_child(folium.Element(legend_html))

m.save('connected_graph.html')