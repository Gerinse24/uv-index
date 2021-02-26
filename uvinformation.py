#! python3

import uvdownload
import re
import uvcategories
import uvlocations

r = uvdownload.main()

pattern = re.compile('"\$\w+":"\w+","\w+":"\w+-\w+-\w+ \w+:\w+","\w+":\w+.\w+,"\w+":\w+.\w+')
matches = re.findall(pattern, r)

# matches[i] is something like "$id":"841","Date":"2021-02-25 19:59","Forecast":0.0,"Measured":0.01012686
# First it is split at , which returns a list.
# Next strip away the part as below, and append the remainder of string to measured.
measured = []
for i in range(len(matches)):
    datasplit = matches[i].split(',')
    measured.append(datasplit[3].strip('"Measured":'))

# We'll need to convert the string at measured[t] into a float.
# maxuv is set to 0.0 as the maxuv will be much larger.
# Iterate through measured by length of itself. Perform conditional check and save highest value.
maxuv = 0.0
for t in range(len(measured)):
    try:
        if float(measured[t]) > maxuv:
            maxuv = float(measured[t])
    except ValueError:  # Sometimes measured[t] is null. If null, uv not measured yet.
        # pass
        break
print(maxuv)

# # TODO: Utilize uvcategories to properly format data and write to csv file.
for k in range(len(matches)):
    datasplit = matches[k].split(',')
    categories = uvcategories.uv_data(datasplit[0], datasplit[1], datasplit[2], datasplit[3])
