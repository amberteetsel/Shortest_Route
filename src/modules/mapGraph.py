from modules.graph import Graph
import folium
import random
import numpy as np

def build_graph_from_json(data, scenario, uncertainty=False):
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

    # Get appropriate travel times for edge weights
    def get_weight(edge_data):
        if scenario == "avg" and not uncertainty:
            return edge_data['avg_time_min']
        elif scenario == "avg" and uncertainty:
            if random.random() < 0.8:
                return edge_data['avg_time_min']
            else:
                return float('inf') if random.random() <= 0.5 else edge_data['avg_time_min'] * 10
        elif scenario == "peak" and not uncertainty:
            mean = 2
            std = 0.5
            return edge_data['avg_time_min'] * max(np.random.normal(mean, std), 0.1)  # avoid zero or negative times
        elif scenario == "peak" and uncertainty:
            mean = 2
            std = 0.5
            if random.random() < 0.8:
                return edge_data['avg_time_min'] * max(np.random.normal(mean, std), 0.1)
            else:
                if random.random() <= 0.5:
                    return float('inf')
                else:
                    return edge_data['avg_time_min'] * max(np.random.normal(mean, std), 0.1) * 10
        else:
            # Default fallback, avg time
            return edge_data['avg_time_min']

    # Add edges
    for from_id, connections in pairwise.items():
        from_name = nodes[from_id]["name"]
        u = id_map[from_name]

        for to_id, edge_data in connections.items():
            to_name = nodes[to_id]["name"]
            v = id_map[to_name]
            w = get_weight(edge_data)

            g.adj_matrix[u][v] = w
            g.adj_matrix[v][u] = w

    return g, id_map, index_to_node_id

