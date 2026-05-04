import osmnx as ox

def build_road_network(place="Rajshahi, Bangladesh"):
    print("Downloading road network...")
    graph = ox.graph_from_place(place, network_type="drive")
    return graph