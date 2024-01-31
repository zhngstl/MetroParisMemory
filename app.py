from flask import Flask, render_template, jsonify
import json
import folium

app = Flask(__name__)

@app.route('/')
def index():
    """
    Homepage: show map + score
    """ 
    # Load the GeoJSON file for the métro stations 
    with open("./data/metro_station.geojson") as f: 
        stations = json.load(f) # Load the GeoJSON file for the métro lines 
    with open("./data/metro_lines.geojson") as f: 
        lines = json.load(f) 

    return render_template('index.html', stations=stations, lines=lines)
