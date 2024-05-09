import pandas as pd
from TenantRecommendation.tenant_functions import get_coordinates, find_common_area, find_common_price_area, find_nearest_neighbours, Locations_on_Price, show_picks

# Reading Dataset on Houses
Houses = pd.read_csv("TenantRecommendation/Houses_2023.csv")

def house_recommendation(loc1, loc2, loc3, price):

    # To Store preferred locations
    loc = []
    indices = []
    lat = []
    lon = []

    loc.append(loc1)
    loc.append(loc2)
    loc.append(loc3)

    for i in range(0, 3):
    
        # Finding Coordinates of Location:
        latitude, longitude = get_coordinates(loc[i])
        lat.append(latitude)
        lon.append(longitude)

        # Using K-Nearest Neighbour Model to find Nearest Locations:
        index = find_nearest_neighbours(Houses, lat[i], lon[i])
        indices.append(index)
    
    # Finding Common locations from each preferred locations
    common = find_common_area(indices)

    # Finding Best Locations Based on Price
    price_index = Locations_on_Price(Houses, price)

    # Finding Intersection of Common Areas and Area within Price Range
    final_common_areas = find_common_price_area(common, price_index)

    # If no common rental property exist between all three preferred locations
    if len(final_common_areas) == 0:
        print("\n*** No Result Matches Your Query. Please Try Something Else :) ***")
  
    else: 
        # Show the Best Stay Locations to User
        recommendations = show_picks(final_common_areas, Houses)
        return recommendations