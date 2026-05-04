from itertools import permutations
from src.routing import shortest_path, path_distance

def optimize_routes(graph, warehouse, delivery_points):
    best_route = None
    min_distance = float('inf')

    for perm in permutations(delivery_points):
        route = [warehouse] + list(perm)
        total_dist = 0

        for i in range(len(route)-1):
            path = shortest_path(graph, route[i], route[i+1])
            total_dist += path_distance(graph, path)

        if total_dist < min_distance:
            min_distance = total_dist
            best_route = route

    return best_route, min_distance
