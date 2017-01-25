"""This module contains the solution for the flight paths Kata for Codefellows 401 Python course."""
from weighted_graph import WGraph

import json

# This function is provided for the class.
def calculate_distance(point1, point2):
    """
    Calculate the distance (in miles) between point1 and point2.
    point1 and point2 must have the format [latitude, longitude].
    The return value is a float.

    Modified and converted to Python from: http://www.movable-type.co.uk/scripts/latlong.html
    """
    import math

    def convert_to_radians(degrees):
        return degrees * math.pi / 180

    radius_earth = 6.371E3 # km
    phi1 = convert_to_radians(point1[0])
    phi2 = convert_to_radians(point2[0])
    delta_phi = convert_to_radians(point1[0] - point2[0])
    delta_lam = convert_to_radians(point1[1] - point2[1])


    a = math.sin(0.5 * delta_phi)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(0.5 * delta_lam)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return radius_earth * c / 1.60934 # convert km to miles


def get_airport_data():
    """Parse airports from provided JSON file into usable format."""
    with open('cities_with_airports.json', 'r') as f:
        data = json.load(f)
        return data


def parse_airport_data():
    """Parse the airport data into a convenient format."""
    data = get_airport_data()
    airport_dict = {}
    for city in data:
        airport_dict[city["city"]] = {
            "lat_long": city["lat_lon"],
            "neighbors": city["destination_cities"]
        }
    return airport_dict


def build_graph_with_data():
    """Return a weighted graph with airport data."""
    airports = parse_airport_data()
    air_graph = WGraph()
    for city, city_data in airports.items():
        city_1 = city
        neighbors = city_data["neighbors"]
        for neighbor in neighbors:
            try:
                dist_between = calculate_distance(
                    city_data["lat_long"],
                    airports[neighbor]["lat_long"]
                )
            except KeyError:
                continue
            air_graph.add_edge(city_1, neighbor, dist_between)
    return air_graph


def find_shortest_flight_path(city_1, city_2):
    """Given two cities, find the shortest path between them."""
    flight_paths = build_graph_with_data()
    try:
        return flight_paths.shortest_dijkstra(city_1, city_2)
    except KeyError:
        print("No flight path exists between those two cities.")
