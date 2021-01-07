#! python3
import csv
import os
import shutil
"""Uvtest.py downloads a csv file containing minute-to-minute uvlevel updates.
The aim of this script is to work with that file and display the maximum uvlevel
so far for that day."""

usrpath = os.path.join(os.path.expanduser('~'), "Downloads")
shutil.move(usrpath + "\\ARPANSA_Charts.csv", os.getcwd())
# TODO: Wrap the above two lines into a function with error handling.
# Make sure that it runs before max_uv()
data = open('ARPANSA_Charts.csv', newline="")
datareader = csv.reader(data)

def max_uv():
    global t
    t = 0.0
    for row in datareader:
        if row[3] == "Measured":
            continue
        if row[3] == '':
            continue
        if float(row[3]) > t:
            t = float(row[3])

max_uv()
print("The maximum UV Level today was %s" % (t))
data.close()
