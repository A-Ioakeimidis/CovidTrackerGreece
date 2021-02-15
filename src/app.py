import os
import webbrowser

import folium
import requests


# Creates the request and Json response
def create_request_and_response():
    try:
        response = requests.get('https://covid-19-greece.herokuapp.com/regions')
        data = response.json()
        return data
    except:
        print("An error occurred while retrieving data")


# Creates the folium map
def create_map():
    covid_map = folium.Map(location=[39.0742, 21.8243], zoom_start=7, tiles="cartodbpositron")
    covid_map.save("CovidMapGreece.html")
    return covid_map


# Add details to popup marker
def add_popup_details(details):
    full_details = "Cases : {} \n Population: {}".format(details['total_cases'], details['population'])
    return full_details


# Adds the markers to the map. Displays total cases for each major city
def add_markers_to_map(data, covid_map):
    feature_group = folium.FeatureGroup(name='CovidMapGreece')
    for coords in data['regions']:
        feature_group.add_child(
            folium.Marker(location=[coords['latitude'], coords['longtitude']], popup=add_popup_details(coords),
                          icon=folium.Icon(color='red')))
        covid_map.add_child(feature_group)
        covid_map.save("CovidMapGreece.html")
        str(coords['total_cases'])


def open_map_from_html():
    filename = 'file:///' + os.getcwd() + '/' + 'CovidMapGreece.html'
    webbrowser.open_new_tab(filename)


# Call the application
api_data = create_request_and_response()
created_map = create_map()
add_markers_to_map(api_data, created_map)
open_map_from_html()
