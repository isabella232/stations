#!/usr/bin/env python
import csv

class Station(object):
    FIELDS = ['City', 'Station', 'Frequency']

    def __init__(self, **kwargs):
        for field in self.FIELDS:
            item = kwargs.get(field, None)
            if item:
                setattr(self, field.lower(), kwargs.get(field))

def init():
    """
    All the things we'd want to do if we called this module from the command line.
    """
    stations = parse_stations_csv()
    for station in stations:
        print station.__dict__

def parse_stations_csv():
    with open('data/stations.csv', 'rU') as readfile:
        stations = list(csv.DictReader(readfile))

    station_list = []

    for station in stations:
        s = Station(**station)
        station_list.append(s)

    return station_list

if __name__ == '__main__':
    init()