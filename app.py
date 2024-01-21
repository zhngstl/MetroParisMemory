from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

@app.route('/')
def index(): 
    # Load the GeoJSON file for the métro stations 
    with open("./data/emplacement-des-gares-idf.geojson") as f: 
        stations = json.load(f) # Load the GeoJSON file for the métro lines 
    with open("./data/traces-du-reseau-ferre-idf.geojson") as f: 
        lines = json.load(f) 
    
    return render_template('index.html', stations=stations, lines=lines)
