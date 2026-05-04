import folium

def create_map(center):
    return folium.Map(location=center, zoom_start=12)

def plot_points(map_obj, gdf, color="blue"):
    for _, row in gdf.iterrows():
        folium.Marker(
            location=[row.geometry.y, row.geometry.x],
            icon=folium.Icon(color=color)
        ).add_to(map_obj)

def plot_route(map_obj, coords):
    folium.PolyLine(coords, color="red", weight=4).add_to(map_obj)