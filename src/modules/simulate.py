from modules.graph import Graph
import json
import numpy as np
import random

def sim_traffic_data(data, start:str, scenario:str, uncertainty=False):
    '''
    scenario=["avg", "peak"]
    uncertainty=[True, False]
    '''
    g = Graph(len(data['nodes']))

    # Average Traffic, no Uncertainty
    if scenario == "avg" and uncertainty == False:
        for key in data['nodes'].keys():
            g.add_vertex_data(int(key), data['nodes'][key]["name"])

        for i in data["pairwise"].keys():
            for j in data["pairwise"][i].keys():
                g.add_edge(int(i), int(j), data["pairwise"][i][j]['avg_time_min'])

    # Average Traffic w/ Uncertainty
    if scenario == "avg" and uncertainty == True:
        for key in data['nodes'].keys():
            g.add_vertex_data(int(key), data['nodes'][key]["name"])

        for i in data["pairwise"].keys():
            for j in data["pairwise"][i].keys():
                rand_val = random.random() 
                if rand_val < 0.8:
                    # No disruption
                    g.add_edge(int(i), int(j), data["pairwise"][i][j]['avg_time_min'])
                else:
                    # Add disruption
                    rand_val2 = random.random()
                    if rand_val2 <= 0.5:
                        # By making weight for the edge 0
                        g.add_edge(int(i), int(j), float('inf'))
                    else:
                        # By making weight for the edge weight 10x
                        g.add_edge(int(i), int(j), data["pairwise"][i][j]['avg_time_min']*10)

    # Peak Traffic, no Uncertainty
    if scenario == "peak" and uncertainty == False:
        for key in data['nodes'].keys():
            g.add_vertex_data(int(key), data['nodes'][key]["name"])

        mean = 2
        std = 0.5
        for i in data["pairwise"].keys():
            for j in data["pairwise"][i].keys():
                g.add_edge(int(i), int(j), data["pairwise"][i][j]['avg_time_min']*np.random.normal(mean, std))

    # Peak Traffic w/ Uncertainty
    if scenario == "peak" and uncertainty == True:
        for key in data['nodes'].keys():
            g.add_vertex_data(int(key), data['nodes'][key]["name"])

        mean = 2
        std = 0.5
        for i in data["pairwise"].keys():
            for j in data["pairwise"][i].keys():
                rand_val = random.random()
                if rand_val < 0.8:
                    g.add_edge(int(i), int(j), data["pairwise"][i][j]['avg_time_min']*np.random.normal(mean, std))
                else:
                    rand_val2 = random.random()
                    if rand_val2 <= 0.5:
                        # Make edge value 0
                        g.add_edge(int(i), int(j), float('inf'))
                    else:
                        # make edge weight 10x
                        g.add_edge(int(i), int(j), data["pairwise"][i][j]['avg_time_min']*np.random.normal(mean, std)*10)

        

    # Output graph, distances
    d = g.dijkstra(start)
    return g, d