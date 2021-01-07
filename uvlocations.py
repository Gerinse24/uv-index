#! python3
# Created by Geronimo Shaw
"""These are the locations of the ARPANSA UV Radars. The dictionary contains
the city names and their corresponding index in the drop-down list.
Refer to uvdownload.py."""

def location_index(place):
    id_dict = {'Canberra': 1,
    'Newcastle': 3,
    'Sydney': 4,
    'Alice Springs': 6,
    'Darwin': 7,
    'Brisbane': 9,
    'Emerald': 10,
    'Gold Coast': 11,
    'Townsville': 12,
    'Adelaide': 14,
    'Kingston': 16,
    'Melbourne': 18,
    'Perth': 20,
    'Casey': 22,
    'Davis': 23,
    'Macquarie Island': 24,
    'Mawson': 25}

    if place in id_dict.keys():
        return id_dict[place]
