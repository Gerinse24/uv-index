# uv-index
This is a script that I use for gathering UV Radiation indexes.

Firstly, the data downloaded is provided by ARPANSA - an agency in the Australian Government. This data is provided under Freedom of Information and cannot be used for financial gain. 

uvindex.py was written in Python 3 using xml.etree.ElementTree submodule for handling the xml file, the requests module to download the xml file, and the sys module for command line usage.

# usage
From CMD, make sure your current working directory contains the scripts you need: uvdata.py and uvindex.py.
If you have not run uvdata.py before, make sure you run it before uvindex.py or you won't have the xml file and uvindex.py will not work.
This can be done in your cwd as such: python uvdata.py

One that is done, you simply run uvindex.py with one argument: python uvindex.py city
city must be an acronym of the cities data you want: python uvindex.py mel
mel meaning Melbourne.
