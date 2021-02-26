#! python 3

import uvlocations
from datetime import date
import requests

def main():
    # Grab current date.
    # Format today into correct_format string for use in request.
    today = date.today()
    correct_format = today.strftime("%Y-%m-%d")

    # A dict of radar locations is in the uvlocations.py script as cities.
    # The location_index() function in uvlocations contains a dictionary with the
    # cities as keys() and their unique URLs as values.
    for city in uvlocations.cities:
        print(city)
    choice = input("Type your choice and press Enter.\n")
    r = requests.get("https://uvdata.arpansa.gov.au/" + uvlocations.location_index(choice) + '&date=' + correct_format).text

    return r
