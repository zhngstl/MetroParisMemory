document.addEventListener('DOMContentLoaded', function() {
    // Initialize Leaflet map
    var map = L.map('map').setView([48.8566, 2.3522], 12); // Default view set to Paris

    // Initialize the map with Carto style
    var CartoDB_PositronNoLabels = L.tileLayer('https://{s}.basemaps.cartocdn.com/light_nolabels/{z}/{x}/{y}{r}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
        subdomains: 'abcd',
        maxZoom: 20
    }).addTo(map);

    function showPopup(popup) {
        popup.style.display = 'block';
    }

    function closePopup() {
        aboutPopup.style.display = 'none';
    }
    
    // Sample marker for testing
    L.marker([48.8566, 2.3522]).addTo(map);

    // Load data to draw each Métro line + station
    function station_loadJSON(station) {
        JSON.parse(station);
    }
    function lines_loadJSON(lines) {
        JSON.parse(lines);
    }
    var stations = station_loadJSON(station);
    var lines = lines_loadJSON(lines);
    
    var lineColors = {};
    lines.features.forEach(function(feature) {
        var properties = feature.properties;
        
        // Check if the "METRO" property is true
        if (properties.metro === 1) {
            var coordinates = feature.geometry.coordinates.map(function(coord) {
                return [coord[1], coord[0]];  // Swap latitude and longitude for Leaflet
            });
            
            var indice_line = Number(feature.properties.indice_lig);
            lineColors[indice_line] = feature.properties.colourweb_hexa;
            
            L.polyline(coordinates, { color: '#' + lineColors[indice_line] }).addTo(map);
        }
    });
});
