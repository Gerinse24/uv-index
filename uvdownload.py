#! python 3

from msedge.selenium_tools import EdgeOptions, Edge
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import uvlocations
import time

# Configure options for driver.
options = EdgeOptions()
options.use_chromium = True
# # TODO: Set download location for browser or get the users path user downloads
# #       folder and move the csv file to the cwd. This could be done in another
# #       script, possibly uvinformation.py

usr_input = input("City?\n")
# Call driver at path with options argument.
driver = Edge("C:\\code\\WebDrivers\\msedgedriver.exe", options=options)
driver.get("https://uvdata.arpansa.gov.au/uvlevel")

# Locate Element which is drop-down list and make selection.
element = WebDriverWait(driver, 10, 2).until(EC.presence_of_element_located((By.ID,
'slctCategoryLocation')))
"""uvlocations.py includes a function which contains the city names and their
indexes for selection."""
if type(element) == type(element):
    drp = Select(element)
    loc_id = uvlocations.location_index(usr_input)
    time.sleep(10)
    drp.select_by_index(loc_id)

# This section is webbrowser automation to download a csv file.
dlmenu = WebDriverWait(driver, 10, 2).until(EC.element_to_be_clickable((By.XPATH,
'//*[@id="chartdiv"]/div/div[3]/ul/li/a')))
actions = ActionChains(driver)
actions.move_to_element(dlmenu)
actions.click()
actions.perform()

saveopt = WebDriverWait(driver, 10, 2).until(EC.element_to_be_clickable((By.XPATH,
'//*[@id="chartdiv"]/div/div[3]/ul/li/ul/li[2]/a/span')))
actions.move_to_element(saveopt)
actions.click()
actions.perform()

savecsv = WebDriverWait(driver, 10, 2).until(EC.element_to_be_clickable((By.XPATH,
'//*[@id="chartdiv"]/div/div[3]/ul/li/ul/li[2]/ul/li[1]/a/span')))
actions.move_to_element(savecsv)
actions.click()
actions.perform()

time.sleep(10)
driver.quit()
