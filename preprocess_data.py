import json

def main():
    stations = load_data("emplacement-des-gares-idf.geojson")
    lines = load_data("traces-du-reseau-de-transport-ferre-idf.geojson")


def load_data(pathfile):
    with open(pathfile, 'r') as file:
        return json.load(file)

class Station:
    def __init__(self, id: int, name: str, line: list[int]) -> None:
        if not name:
            raise ValueError("Missing name")
        if not line:
            raise ValueError("Missing line")
        self.name = name
        self.line = line
        
    
    stations = []

    for feature in metro_data['features']:
        station_name = feature['properties']['nom_zdc']
        metro_lines = feature['properties']['res_com']
        coordinates = feature['geometry']['coordinates']

        # You can store this information in a list or dictionary
        station_info = {
            'name': station_name,
            'lines': metro_lines,
            'coordinates': coordinates
        }

        stations.append(station_info)