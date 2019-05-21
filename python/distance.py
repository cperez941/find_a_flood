""" Author : Carl Perez
    Description : Gets the nearest river info of a category
"""
import database
import requests
from math import sin, cos, sqrt, atan2, radians

# approximate radius of earth in km
RADIUS_EARTH = 6373.0

def convert_km_to_mi(km):
    """ convert kilometers to miles
    Args:
        km - kilometers to be converted
    Returns:
        mi - the converted values
    """
    mi = 0.621371 * float(km)
    return mi


def compare_long_lat(coord, category="Major_Stage"):
    """ Gives the kilometer distance between a point and all rivers of
        a category, using derivation of haversine formula from:
        https://andrew.hedges.name/experiments/haversine/
    Args:
        coord - a tuple containing coords, lat then long
        category - a category of river flooding stage
    Returns:
        distances - a float of the distance
    """
    # init vars
    lat_point, lon_point = coord
    distances = []

    for lat_river, lon_river in database.collect_coord(category):
        d_lon = radians(abs(lon_river)) - radians(abs(lon_point))
        d_lat = radians(abs(lat_river)) - radians(abs(lat_point))
        print(lat_point, lon_point)
        print(lat_river, lon_river)

        side_a = (sin(d_lat / 2)**2 + cos(radians(abs(lat_point))) * \
                  cos(radians(abs(lat_river))) * sin(d_lon / 2)**2)
        side_c = 2 * atan2(sqrt(side_a), sqrt(1 - side_a))

        distance = RADIUS_EARTH * side_c
        distance = convert_km_to_mi(distance)
        distances.append(distance)

    return distances
