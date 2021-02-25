# uv-index
UV observations courtesy of ARPANSA. This data cannot be used for financial gain, as specified by Australian Radiation Protection and Nuclear Safety Agency.
The aim of uv-index is to provide quick and dirty UV information. This so far is limited to providing the maximum uv level depending on which city and the time of day this data is downloaded. 

Functionality is split between three scripts for readability, and development.

# uvlocations.py
This script has a single function `location_index(place)` which contains a dictionary of accepted locations as the `keys()`, and their corresponding API URL as the `values()` for the radars raw data. `location_index()` will return the value IF it is present in the dictionary.

# uvdownload.py
This script contains most of the functionality but is incomplete as of right now. For now though, uvdownload.py uses the requests module to request the raw data from ARPANSA's API and the response data returned with the `.text` attribute is stored in variable `r`. A regex pattern is used to `findall()` the data that matches, and the garbage is split away through iterating the list of matches until we have a list of `measured` values. A `try and except` block is used to perform conditional checks on each measured value as not all measurements will contain floats - some may contain the word null as no measurement has been made yet.

# This documentation is incomplete, as the script is in early idea stage.
