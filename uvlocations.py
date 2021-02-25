#! python3
"""These are the locations of the ARPANSA UV Radars. The dictionary contains
the city names and their corresponding index in the drop-down list.
Refer to uvdownload.py."""

def location_index(place):
    id_dict = {'Canberra': "api/uvlevel/?longitude=149.2&latitude=-35.31",
    'Newcastle': "api/uvlevel/?longitude=151.72&latitude=-32.9",
    'Sydney': "api/uvlevel/?longitude=151.1&latitude=-34.04",
    'Alice Springs': "api/uvlevel/?longitude=133.89&latitude=-23.8",
    'Darwin': "api/uvlevel/?longitude=130.89&latitude=-12.43",
    'Brisbane': "api/uvlevel/?longitude=153.03&latitude=-27.45",
    'Emerald': "api/uvlevel/?longitude=148.161346&latitude=-23.5251",
    'Gold Coast': "api/uvlevel/?longitude=153.37&latitude=-28",
    'Townsville': "api/uvlevel/?longitude=146.76&latitude=-19.33",
    'Adelaide': "api/uvlevel/?longitude=138.52&latitude=-34.95",
    'Kingston': "api/uvlevel/?longitude=147.29&latitude=-42.99",
    'Melbourne': "api/uvlevel/?longitude=145.1&latitude=-37.73",
    'Perth': "api/uvlevel/?longitude=115.98&latitude=-31.93",
    'Casey': "api/uvlevel/?longitude=110.53&latitude=-66.28",
    'Davis': "api/uvlevel/?longitude=77.97&latitude=-68.58",
    'Macquarie Island': "api/uvlevel/?longitude=158.94&latitude=-54.5",
    'Mawson': "api/uvlevel/?longitude=62.87&latitude=-67.6"}

    if place in id_dict.keys():
        return id_dict[place]

locations = ['Canberra', 'Newcastle', 'Sydney', 'Alice Springs', 'Darwin',
'Brisbane', 'Emerald', 'Gold Coast', 'Townsville', 'Adelaide', 'Kingston',
'Melbourne', 'Perth', 'Casey', 'Davis', 'Macquarie Island', 'Mawson']
