from geopy.geocoders import Nominatim
import json
import pandas as pd
import gmplot

def newsMap(json_news, output_path, api_key):
    print('Opening Your Json File...')
    with open(f'{json_news}', 'r', encoding='utf-8') as fp:
        data = json.load(fp)
    print('Done')

    print('Getting the Coordenates...')
    locations = []
    for i in data:
        locations.append(i['Locations'])

    coordenates = []

    geolocator = Nominatim(user_agent="123@python.com")

    x = 1
    for loc in locations:
        location = geolocator.geocode(loc, timeout=10000)
        if loc == None:
            coordenates.append((None, None))
        else:
            try:
                coordenates.append((location.latitude, location.longitude))
            except:
                coordenates.append((None, None))
        print(f'Coordenate {x} out of {len(locations)}')
        x = x + 1
    print('Done')

    print('Plotting...')
    stop_words = []

    newLocations = []
    newCoordenates = []
    Locindex = []
    newIndex = []

    for i in range(len(coordenates)):
        if coordenates[i] != [None, None]:
            newCoordenates.append(coordenates[i])
            Locindex.append(i)

    for index in Locindex:
        newLocations.append(locations[index])

    for i in stop_words:
        if i in newLocations:
            newIndex.append(newLocations.index(i))
            newLocations.remove(i)

    for index in newIndex:
        newCoordenates.remove(newCoordenates[index])

    apikey = api_key

    gmap = gmplot.GoogleMapPlotter(39.399872, -8.224454, 8, apikey=apikey, encoding="utf-8", map_type='hybrid')

    i = 0
    for lat, lon in newCoordenates:
        if lat != None:
            locName = newLocations[i]
            linkName = f'https://www.google.com/maps/place/{locName}'
            gmap.marker(lat, lon, info_window=f"<a href='{linkName}'>{locName}</a>", encoding="utf-8")
            print(locName)
            i = i + 1
        continue

    gmap.draw(f"{output_path}.html")
    print('Done')

