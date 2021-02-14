import requests
import json
import folium

#Creates the request and Json response
def create_request_and_response():
    try:
        response = requests.get('https://covid-19-greece.herokuapp.com/regions')
        data = response.json();
        return data
    except:
        print("An error occured while retrieving data")

#Creates the folium map
def create_map():
    map = folium.Map(location=[39.0742, 21.8243], zoom_start=7, tiles="cartodbpositron")
    map.save("CovidMapGreece.html")
    return map

#Adds the markers to the map. Displays total cases for each major city
def add_markers_to_map(data, map):
    feature_group = folium.FeatureGroup(name = 'CovidMapGreece')
    for coords in data['regions']:
        feature_group.add_child(folium.Marker(location=[coords['latitude'], coords['longtitude']], popup="Cases: " + str(coords['total_cases']), icon=folium.Icon(color='red')))
        map.add_child(feature_group)
        map.save("CovidMapGreece.html")
        str(coords['total_cases'])

#Call the application
api_data = create_request_and_response()
created_map = create_map()
add_markers_to_map(api_data, created_map)       