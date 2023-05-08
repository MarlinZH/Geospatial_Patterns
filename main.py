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
    test