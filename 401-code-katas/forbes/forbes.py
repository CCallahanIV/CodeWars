"""This module contains the solution for the forbes top 40 kata."""

import json


def get_json_data_from_file(file):
    """Return JSON data given a filename."""
    with open(file, 'r') as f:
        data = f.read()

    return json.loads(data)


def find_rich_people():
    """Find the oldest rich guy under 80."""
    data = get_json_data_from_file("forbes.json")

    rich_old_person = max([person for person in data if person["age"] < 80], key=lambda x: x["age"])
    rich_young_person = min([person for person in data if person["age"] > 0], key=lambda x: x["age"])
    return rich_old_person, rich_young_person


# The requests library and beautiful soup are required for the next function.


import requests
import re
from bs4 import BeautifulSoup as Soup


def find_current_stock_price(company):
    """Find the stock price for a given company."""
    payload = {'q': company}
    resp = requests.get("http://www.google.com/search?", payload)
    html = Soup(resp.content, "html.parser")
    try:
        stock_price = html.find("span", text=re.compile('(\$[0-9]+\.[0-9]+)')).text
        return "Stock Price for {} is {}".format(company, stock_price)
    except AttributeError:
        return "No price for that company."
