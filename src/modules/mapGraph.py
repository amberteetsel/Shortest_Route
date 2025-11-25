from modules.graph import Graph
import folium

def build_graph_from_json(data, scenario):
    '''
    scenario = ["avg", "peak"]
    '''
    if scenario=="avg":
        metric = "avg_time_min"
    if scenario=="peak":
        metric = "peak_time_min"
        
    nodes = data["nodes"]
    pairwise = data["pairwise"]

    node_list = list(nodes.items())
    size = len(node_list)
    g = Graph(size)

    id_map = {}
    index_to_node_id = {}
    for i, (node_id, node_data) in enumerate(node_list):
        id_map[node_data["name"]] = i
        index_to_node_id[i] = node_id
        g.add_vertex_data(i, node_data["name"])

    # Add edges
    for from_id, connections in pairwise.items():
        from_name = nodes[from_id]["name"]
        u = id_map[from_name]

        for to_id, edge_data in connections.items():
            to_name = nodes[to_id]["name"]
            v = id_map[to_name]
            w = edge_data.get(metric, 0)

            g.adj_matrix[u][v] = w
            g.adj_matrix[v][u] = w

    return g, id_map, index_to_node_id

