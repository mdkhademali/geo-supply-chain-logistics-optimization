import networkx as nx

def get_nearest_node(graph, point):
    return nx.distance.nearest_nodes(graph, point.x, point.y)

def shortest_path(graph, source, target):
    return nx.shortest_path(graph, source, target, weight="length")

def path_distance(graph, path):
    distance = 0
    for u, v in zip(path[:-1], path[1:]):
        distance += graph[u][v][0].get("length", 0)
    return distance