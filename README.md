# uv-index
UV observations courtesy of ARPANSA. This data cannot be used for financial gain, as specified by Australian Radiation Protection and Nuclear Safety Agency.
The aim of uv-index is to provide quick and dirty UV information. This so far is limited to providing the maximum uv level depending on which city and the time of day this data is downloaded. 

Functionality is split between three scripts for readability, and development.

# uvlocations.py
This script has a single function `location_index(place)` which contains a dictionary of accepted locations as the `keys()`, and their corresponding index as the `values()` for when selenium interacts with a drop-down menu in uvdownload.py. Once the index is located and confirmed, `location_index(place)` will return the index so selenium automation can make the selection.

# uvdownload.py
This script will perform web automation by interacting with ARPANSA's API. The interactions are `move_to_element()`, `click()`, and `perform()` which are provided by `selenium.webdriver.common.action_chains`. They are used to make city selection from a drop-down menu, and then to `click()` the API's download button. The browser used for automation is MSEdge Chromium which you will need to download from [here](https://docs.microsoft.com/en-us/microsoft-edge/webdriver-chromium/?tabs=python). uvdownload.py's success is intermittent, and this comes down to dealing with dynamic content.

# uvinformation.py 
This script peforms actions on the CSV file downloaded by uvdownload.py. The `os.path.expanduser()` function from the `os` module is used to determine the user path, and `os.path.join` that with the string Downloads, this is then passed to `shutil.move()` along with the new destination.
