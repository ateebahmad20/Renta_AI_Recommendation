# Importing Required Libraries
from geopy.geocoders import Nominatim
from sklearn.neighbors import KNeighborsClassifier

# Function to get coordinates of a location
def get_coordinates(loc):

  # Setting up the Agent
  Locator_agent = Nominatim(user_agent="location_details")

  # Finding Coordinates
  location = Locator_agent.geocode(loc, timeout=None)

  # If not found
  if location is None:
    print("No Such Location Found. Please Try Another Location")

  else:
      # Returning Coordinates:
      return location.latitude, location.longitude

# Function to find Optimum location Based on Price
def Locations_on_Price(Houses, price):

  index = []

  # filtering data based on Price
  for i in range(0, len(Houses)):
    if Houses["Rent"][i] < price:
      index.append(i)
  
  return index

# Function to Find the Best Location for User
def find_nearest_neighbours(Houses, lat, lon):
  
  # Extracting Required Features from the Dataset
  features = Houses.loc[:,["Latitude", "Longitude"]]
  y = Houses.loc[:,["neighbourhood"]]

  # Implementing K nearest neighbous classifier
  # Here, K = 500
  K = 500
  knn = KNeighborsClassifier(K)

  # Fitting the Model
  knn.fit(features.values, y.values.ravel())

  # Finding Nearest Locations from the User's Preferred Location:
  i = knn.kneighbors([[lat, lon]], n_neighbors = K, return_distance = False)

  # Converting index to a 1-d Array
  index = i.ravel()
  return index

# Function for Showing the Results
def show_picks(index, Houses):

  recommendations = []

  for i in range(0, len(index)):

    location = Houses["neighbourhood"][index[i]]
    area = Houses["neighbourhood_group"][index[i]]
    marla = int(Houses["Area"][index[i]])
    lat = float(Houses["Latitude"][index[i]])
    lon = float(Houses["Longitude"][index[i]])  # Convert to float
    bath = int(Houses["Bath_s_"][index[i]])  # Convert to int
    beds = int(Houses["Bedroom_s_"][index[i]])  # Convert to int
    rent = int(Houses["Rent"][index[i]])  # Convert to int
    crimeRate = Houses["Crime Rate"][index[i]]  # Convert to float

    recommendations.append({"Location": location, "Area": area, "Marla": marla, "Latitude": lat, "Longitude": lon,
                            "Bathrooms": bath, "Bedrooms": beds, "Rent(K)": rent, "Crime Rate": crimeRate})
      
  return recommendations
   
# Function for find common area from all preferred locations
def find_common_area(indices):

  c = [value for value in indices[0] if value in indices[1]]
  common = [value for value in indices[2] if value in c]

  return common

# Function for Finding Intersection of Common Areas and Area within Price Range
def find_common_price_area(common_areas, price_areas):

  common = [value for value in common_areas if value in price_areas]
  return common
