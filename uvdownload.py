#! python 3

import csv
import uvlocations
from datetime import date
import requests
import re

# Grab current date.
# Format today into correct_format string for use in request.
today = date.today()
correct_format = today.strftime("%Y-%m-%d")

# A dict of radar locations is in the uvlocations.py script as locations.
# key/value is city name/url. The URL is triggered through ARPANSA API.
print(uvlocations.locations)
usr_input = input("Enter city name:\n")

r = requests.get("https://uvdata.arpansa.gov.au/" + uvlocations.location_index(usr_input) + '&date=' + correct_format).text

pattern = re.compile('"\$\w+":"\w+","\w+":"\w+-\w+-\w+ \w+:\w+","\w+":\w+.\w+,"\w+":\w+.\w+')
matches = re.findall(pattern, r)

measured = []
for i in range(len(matches)):
    datasplit = matches[i].split(',')
    measured.append(datasplit[3].strip('"Measured":'))

maxuv = 0.0
for t in range(len(measured)):
    try:
        if float(measured[t]) > maxuv:
            maxuv = float(measured[t])
    except ValueError:
        # pass
        break
print(maxuv)
