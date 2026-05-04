from itertools import permutations
from src.routing import shortest_path, path_distance

def solve_vrp(graph, warehouse_node, delivery_nodes):
    best_route = None
    min_cost = float("inf")

    for perm in permutations(delivery_nodes):
        route = [warehouse_node] + list(perm)
        total_cost = 0

        for i in range(len(route)-1):
            path = shortest_path(graph, route[i], route[i+1])
            total_cost += path_distance(graph, path)

        if total_cost < min_cost:
            min_cost = total_cost
            best_route = route

    return best_route, min_cost