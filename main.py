import geopandas as gpd
from shapely.geometry import point, polygon
import osmnx
import shapely
import pandas as pd
import numpy as np
import networkx as nx

def area_boundries(area):
    '''
    Returns the boundary points of an Area bound to cardinal directions
    :param area:
    :return:
    '''
    gdf = osmnx.geocode_to_gdf(area)
    #print(gdf)

    # Gets the bounding box of the gdf GeoDataFrame
    bounding = gdf.bounds
    #print('BOUNDING:', bounding)

    north, south, east, west = bounding.iloc[0, 3], bounding.iloc[0, 1], bounding.iloc[0, 2], bounding.iloc[0, 0]
    #print('North: {},South: {},East: {},West: {}'.format(north, south, east, west))

    location = gdf.unary_union

    return north,south,east,west,location
def area_entities(area,tags):
    '''
    Returns a dataframe of entities in an area grouped by Brand and the quantities of each brand
    :param area:
    :param tags:
    :return:
    '''
    north, south, east, west,location = area_boundries(area)
    print(north, south, east, west)

    # Find Points within the polygon
    point = osmnx.geometries_from_bbox(north, south, east, west, tags)
    print('Point:', point)

    point.set_crs(4326)
    print(point.crs)

    point = point[point.geometry.within(location)]
    point['geometry'] = point['geometry'].apply(lambda x: x.centroid if type(x) == polygon else x)
    point = point[point.geom_type != 'MultiPolygon']
    point = point[point.geom_type != 'Polygon']

    results = pd.DataFrame({'name': list(point['name']),
                            'brand': list(point['brand:en']),
                            'longitude': list(point['geometry'].x),
                            'latitude': list(point['geometry'].y)})
    results['name'] = list(tags.values())[0]
    print(results)
    counrer = results['brand'].value_counts()
    print(counrer)

    results = results.groupby('brand').apply(print)
#
def point_finder(area,tags):
    '''
    Returns a dataframe of coordinates of an entity from OSM.
    :param area(str): A location
    :param tags(dict): key value of entity attribute in OSM and value
    :return: results(DataFrame): table of latitude and longitude with entity value
    '''
    #Creates GeoDataframe of longitude and Latitude of place
    gdf = osmnx.geocode_to_gdf(area)
    print('GDF:',gdf)
    #Gets the bounding box of the gdf GeoDataFrame
    bounding = gdf.bounds
    print('BOUNDING:',bounding)
    north, south, east, west = bounding.iloc[0, 3], bounding.iloc[0, 1], bounding.iloc[0, 2], bounding.iloc[0, 0]
    print('North: {},South: {},East: {},West: {}'.format(north,south,east,west))
    location = gdf.unary_union
    #Find Points within the polygon
    point = osmnx.geometries_from_bbox(north, south, east, west,tags)
    print('Point:',point)
    # p = gpd.GeoDataFrame({'name':['North','South','East','West'],'geometry':[north,south,east,west]})
    # print('P:',p)

    # #point = gpd.GeoDataFrame(p['name'],geometry=p['geometry'])
    # # tags = tags)
    # print('THIS IS THE POINT',point)
    point.set_crs(4326)
    print(point.crs)
    # location = gdf.unary_union
    #print(location)
    point = point[point.geometry.within(location)]
    point['geometry'] = point['geometry'].apply(lambda x:x.centroid if type(x) == polygon else x)
    point = point[point.geom_type != 'MultiPolygon' ]
    point = point[point.geom_type != 'Polygon']

    results = pd.DataFrame({'name':list(point['name']),
                            'longitude':list(point['geometry'].x),
                            'latitude':list(point['geometry'].y)})
    results['name'] = list(tags.values())[0]
    print(results)
    return results
convenience_stores = area_entities(area= 'Shinjuku,Tokyo',tags={"shop":"convenience"})