import geopandas as gpd
from shapely.geometry import point, polygon
import osmnx
import shapely
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def area_boundries(area):
    '''
    Returns the boundary points of an Area bound to cardinal directions
    :param area:
    :return:
    '''
    #Creates GeoDataframe of longitude and Latitude of place
    gdf = osmnx.geocode_to_gdf(area)
    #print('Area GeoDataFrame:',gdf)

    #Gets the bounding box of the gdf GeoDataFrame
    bounding = gdf.bounds
    #print('Bounding:', bounding)

    north, south, east, west = bounding.iloc[0, 3], bounding.iloc[0, 1], bounding.iloc[0, 2], bounding.iloc[0, 0]
    #print('North: {},South: {},East: {},West: {}'.format(north, south, east, west))

    location = gdf.unary_union
    #print('Location:',location)
    return north,south,east,west,location
def area_entities_list(area,tags,output = 'yes'):
    '''
    Returns a dataframe of coordinates of an entity from OSM.
    :param area(str): A location
    :param tags(dict): key value of entity attribute in OSM and value
    :return: results(DataFrame): table of latitude and longitude with entity value
    '''
    north, south, east, west,location = area_boundries(area)
    #print(north, south, east, west)

    # Find Points within the polygon
    point = osmnx.geometries_from_bbox(north, south, east, west, tags)
    #print('Point:', point)

    point.set_crs(4326)
    #print(point.crs)

    point = point[point.geometry.within(location)]
    point['geometry'] = point['geometry'].apply(lambda x: x.centroid if type(x) == polygon else x)
    point = point[point.geom_type != 'MultiPolygon']
    point = point[point.geom_type != 'Polygon']

    entities_list = pd.DataFrame({'OSM Tag': list(tags.values())[0],
                            'Brand': list(point['brand:en']),
                            'longitude': list(point['geometry'].x),
                            'latitude': list(point['geometry'].y)})


    if output == 'yes':
        entities_list = entities_list.groupby('Brand')
        entity_list_output = entities_list.apply(print)
        print('Entities Successfully Listed')
    else:
        print('Entities Successfully Identified')

    return entities_list
def area_entities_count(area,tags):

    entity_list = area_entities_list(area,tags,output='no')
    entity_count = entity_list['Brand'].value_counts()
    print(entity_count)
    return entity_count

entities_in_area = area_entities_count(area= 'Shinjuku,Tokyo',tags={"shop":"convenience"})
plt.pie(entities_in_area,labels=entities_in_area.values)
plt.legend(entities_in_area.index)
entities_list = area_entities_list(area='Shinjuku,Tokyo',tags={"shop":"convenience"})
#Convert location to radians
locations = entities_list[["latitude","longitude"]].values
locations_radians = np.radians(locations)   