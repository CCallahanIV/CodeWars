"""This module contains the tests for the flight paths kata for the Code Fellows Python 401 class."""

import pytest

CITY_1 = "Seattle"
LAT_LONG_1 = [47.44889, -122.30944]

CITY_2 = "Portland (OR)"
LAT_LONG_2 = [45.58861, -122.5975]

CITY_3 = "Amsterdam"
LAT_LONG_3 = [52.30806, 4.76417]

CITY_4 = "Munich"
LAT_LONG_4 = [48.35389, 11.78611]


@pytest.fixture
def graph():
    """Return graph with data."""
    from flight_paths import build_graph_with_data
    return build_graph_with_data()


def test_get_airport_data_returns_json():
    """Test that get_airport_data returns data in JSON format."""
    from flight_paths import get_airport_data
    data = get_airport_data()
    assert data[0]["city"] == "Goma"
    assert data[0]["lat_lon"] == [-1.669889, 29.238278]
    assert data[0]["destination_cities"] == ["Kinshasa", "Kisangani", "Addis Ababa"]
    assert data[1]["city"] == "Kinshasa"


def test_parse_airport_data_returns_expected_format():
    """Test that parse functions returns desired data format."""
    from flight_paths import parse_airport_data
    data = parse_airport_data()
    assert data["Goma"] == {
        'lat_long': [-1.669889, 29.238278],
        'neighbors': ['Kinshasa', 'Kisangani', 'Addis Ababa']
    }


def test_build_graph_returns_weighted_graph(graph):
    """Test that build graph returns a weighted graph with data."""
    assert str(type(graph)) == "<class 'weighted_graph.WGraph'>"


def test_build_graph_returns_w_graph_with_data(graph):
    """Test that build graph returns graph with data."""
    assert len(graph.nodes()) > 0
    assert graph.has_node("Seattle") is True


def test_shortest_path_simple_path():
    """Test that shortest path function returns correct data for simple example."""
    from flight_paths import find_shortest_flight_path
    from flight_paths import calculate_distance
    result = find_shortest_flight_path(CITY_1, CITY_2)
    assert result[0] == ["Seattle", "Portland (OR)"]
    assert result[1] == calculate_distance(LAT_LONG_1, LAT_LONG_2)

def test_shortest_path_med_path():
    """Test the shortest path for a slightly more complicated path."""
    from flight_paths import find_shortest_flight_path
    from flight_paths import calculate_distance
    result = find_shortest_flight_path(CITY_2, CITY_4)
    assert result[0] == [CITY_2, CITY_3, CITY_4]
    total = calculate_distance(LAT_LONG_2, LAT_LONG_3) + calculate_distance(LAT_LONG_3, LAT_LONG_4)
    assert result[1] == total

