#! python3

# uvindex.py - used to quickly grab a Cities UV Index.
# Currently only working for Australia.
# Usage from command line: python uvindex.py city
# city must be an acronym such as per for Perth or mel for Melbourne.

"""Please be advised that the data used for this script is provided by ARPANSA 
and cannot be used for financial gain."""

import xml.etree.ElementTree as ET
import sys

tree = ET.parse('uvdata.xml') # this file is created when you run uvdata.py
root = tree.getroot()

for i in range(len(root)):
    if sys.argv[1] == root[i][0].text:
        print("The UV index as of %s local time is %s" % (root[i][2].text, root[i][1].text))
        break
