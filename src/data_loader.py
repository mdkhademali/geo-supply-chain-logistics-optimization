import geopandas as gpd

def load_warehouses(path):
    return gpd.read_file(path)

def load_delivery_points(path):
    return gpd.read_file(path)