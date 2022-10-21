from geopy.geocoders import Nominatim
import json
import pandas as pd
import gmplot
def newsMap(input_filename, output_filename, api_key):
    path = "data/"
    jsonFile = open(path + input_filename, encoding="utf8")
    data = json.load(jsonFile)

    Locations = []
    Coordinates = []

    geolocator = Nominatim(user_agent='123@python.com')

    for newsarticle in data:
        for location in newsarticle['Locations']:
            # Geo Map
            loc = geolocator.geocode(location, timeout=10000)
            try:
                if location.lower() not in Locations:
                    Coordinates.append((loc.latitude, loc.longitude))
                    Locations.append(location.lower())
            except:
                pass

    # Generate HTML Plot
    gmap = gmplot.GoogleMapPlotter(39.399872, -8.224454, 8, apikey=api_key, encoding="utf-8", map_type='hybrid')

    for i in range(len(Coordinates)):
        lat = Coordinates[i][0]
        lon = Coordinates[i][1]

        if Coordinates[i][0] != None:
            locName = Locations[i]
            linkName = f'https://www.google.com/maps/place/{locName}'
            gmap.marker(lat, lon, info_window=f"<a href='{linkName}'>{locName}</a>", encoding="utf-8")

    gmap.draw(f"{path + output_filename}")

