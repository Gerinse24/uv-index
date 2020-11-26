#! python3

# uvindex.py - used to quickly grab a suburbs UV Index.

import requests
import re
import sys

# make request and store request object.
r = requests.get("http://www.bom.gov.au/places/wa/perth/forecast/")
# searches r.text for any regex matches
# findall returns a list of all matches which will be stored in result
result = re.findall("Sun protection .*", r.text)

for i in range(len(result)):
    if i == 0:
        print("Today: %s" % result[i].strip("</p>   </div>"))
    else:
        print("Then: %s" % result[i].strip("</p>   </div>"))

exit = input("Press X to exit")
if exit.lower() == "x":
    sys.exit()
