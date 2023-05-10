import geopandas as gpd
from shapely.geometry import point, polygon
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
    print('GDF:',gdf)
    bounding = gdf.bounds
    print('BOUNDING:',bounding)
    north, south, east, west = bounding.iloc[0, 3], bounding.iloc[0, 1], bounding.iloc[0, 2], bounding.iloc[0, 0]
    print('North:{},South:{},East:{},West{}'.format(north,south,east,west))
    p = {'name':[place],'geometry':[north,south,east,west]}
    point = osmnx.geometries_from_bbox(north,south,east, west, tags)
    #point = gpd.GeoDataFrame(p['name'],geometry=p['geometry'])
    # tags = tags)
    print('THIS IS THE POINT')
    # point.set_crs(4326)
    print(point.crs)
    location = gdf.unary_union
    print(location)
    # point = point[point.geometry.within(location)]

    # point['geometry'] = point['geometry'].apply(lambda x:x.centroid if type(x) == polygon else x)
    # point = point[point.geom_type != 'MultiPolygon' ]
    # point = point[point.geom_type != 'Polygon']

    results = pd.dataframe({'name':list(point['name']),
                            'longitude':list(point['geometry'].x),
                            'latitude':list(point['geometry'].y)})
    results['name'] = list(tags.values())[0]
    return results
convenience_stores = point_finder(place= 'Shinjuku,Tokyo',tags={"brand:en":""})