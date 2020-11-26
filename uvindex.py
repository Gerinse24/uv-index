#! python3

# uvindex.py - used to quickly grab a suburbs UV Index.

import requests
import re
import sys

# make request to url using two command line arguments.
# sys.argv[1] is the state and sys.argv[2] is the city.
r = requests.get("http://www.bom.gov.au/places/%s/%s/forecast/" % (sys.argv[1], sys.argv[2]))

# searches r.text for any regex matches
# findall returns a list of all matches which will be stored in result
result = re.findall("Sun protection .*", r.text)

# iterate the length of result. result[0] will be the index for today.
# strip the remaining HTML code from result and print to screen.
for i in range(len(result)):
    if i == 0:
        print("Today: %s" % result[i].strip("</p>   </div>"))
    else:
        print("Then: %s" % result[i].strip("</p>   </div>"))

exit = input("Press X to exit")
if exit.lower() == "x":
    sys.exit()
