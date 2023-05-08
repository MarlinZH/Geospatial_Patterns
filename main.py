import geopandas as gpd
from shapely.geometry import Point, Polygon
import osmnx
import shapely
import pandas as pd
import numpy as np
import networkx as nx

def point_finder(place,tags):
    '''
    Returns a dataframe of coordinates of an entity from OSM.
    :param place(str): A location
    :param tags(dict):key value of entity attribute in OSM and value
    :return: results(DataFrame): table of latitude and longitude with entity value
    '''
    gdf = osmnx.geocode_to_gdf(place)
    bounding = gdf.bounds
    north, south, east , west = bounding.iloc[0,3], bounding.iloc[0,1], bounding.iloc[0,2], bounding.iloc[0,0]
    location = gdf.geometry.unarty_union

    point = osmnx.geometries_from_bbox(north,
                                       south,
                                       east,
                                       west,
                                       tags = tags)
    points.set_crs(crs=4326)
    point = point[point.geometry.within(location)]

    point['geometry'] = point[geometry].apply(lambda x:x.centroid if type(x) == Polygon else x)