#! python3

"""uvdata.py downloads and saves uv data in xml format. This is separate from
uvindex.py so multiple requests are not made"""

import requests

r = requests.get('https://uvdata.arpansa.gov.au/xml/uvvalues.xml')

with open('uvdata.xml', 'w+') as file:
    file.write(r.text)

file.close()
