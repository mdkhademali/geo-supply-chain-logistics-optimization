from src.data_loader import load_warehouses, load_delivery_points
from src.network_builder import build_road_network
from src.routing import shortest_path, path_distance
from src.vrp_solver import solve_vrp
from src.visualization import create_map, plot_points, plot_route

import osmnx as ox

# Load data
warehouses = load_warehouses("data/warehouses.geojson")
deliveries = load_delivery_points("data/delivery_points.geojson")

# Build road network
graph = build_road_network()

# Convert to nodes
warehouse_point = warehouses.geometry.iloc[0]
warehouse_node = ox.distance.nearest_nodes(graph, warehouse_point.x, warehouse_point.y)

delivery_nodes = []
for point in deliveries.geometry:
    node = ox.distance.nearest_nodes(graph, point.x, point.y)
    delivery_nodes.append(node)

# Solve routing
best_route, cost = solve_vrp(graph, warehouse_node, delivery_nodes)

print("Best Route:", best_route)
print("Total Cost:", cost)

# Visualization
center = [warehouse_point.y, warehouse_point.x]
map_obj = create_map(center)

plot_points(map_obj, warehouses, "green")
plot_points(map_obj, deliveries, "blue")

# Save map
map_obj.save("outputs/map.html")

print("Map saved to outputs/map.html")