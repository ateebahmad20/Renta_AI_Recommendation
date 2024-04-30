import torch
from TouristRecommendation.tourist_model import Recommender
from TouristRecommendation.tourist_dataset import *
from TouristRecommendation.input import get_ids
import numpy as np
  
model = Recommender(user_classes, location_classes, hotel_classes, hotelRating_classes, price_classes)

#Loading the Model
device = "cuda" if torch.cuda.is_available() else "cpu"
model.load_state_dict(torch.load("model/recommender.pth", map_location=torch.device(device)))

def hotel_recommendations(Name, Location, Price):
    
    ratings = []
    
    # Getting Input
    user, location, price = get_ids(Name, Location, Price)

    # Coverting information to tensors
    user_id = torch.tensor(user)
    location_id = torch.tensor(location)
    price_id = torch.tensor(price)

    ## Getting Ratings for each hotel
    with torch.no_grad():
        for i in range(0,162):
        
            # Filtering
            hotel_name = reverse_hotel_dict[i]
            hotel_rating = df_unique_hotels[df_unique_hotels['hotel'] == hotel_name]['Hotel_rating']
            rating_id = hotelRating_dict[hotel_rating.item()]

            # Predicting
            yhat = model(user_id.view(1), location_id.view(1), torch.tensor(i).view(1), torch.tensor(rating_id).view(1), price_id.view(1))
            ratings.append(yhat)

    # Getting top 20 recommendations:
    ratings = np.array(ratings)
    top_recommendations = np.argsort(ratings.ravel())[-20:][::-1]

    ## Displaying top Recommendations to Users:
    recommendations = []
    for i in range(0,20):

        # Getting Hotel Information
        h_rating = ratings[top_recommendations[i]].item()
        hotel = reverse_hotel_dict[top_recommendations[i]]
        host_name = df_unique_hotels[df_unique_hotels['hotel'] == hotel]['host'].item()
        img = df_unique_hotels[df_unique_hotels['hotel'] == hotel]['images-src'].item()
        location = df_unique_hotels[df_unique_hotels['hotel'] == hotel]['location'].item()
        guest = df_unique_hotels[df_unique_hotels['hotel'] == hotel]['guests'].item()
        beds = df_unique_hotels[df_unique_hotels['hotel'] == hotel]['bedroom'].item()
        bath = df_unique_hotels[df_unique_hotels['hotel'] == hotel]['bath'].item()
        h_price = df_unique_hotels[df_unique_hotels['hotel'] == hotel]['price_per_night($)'].item()
        review = df_unique_hotels[df_unique_hotels['hotel'] == hotel]['Comments'].item()
        crime = df_unique_hotels[df_unique_hotels['hotel'] == hotel]['Crime Rate'].item()

        if h_rating > 5:
            h_rating = 5
        
        recommendations.append({"Hotel": hotel, "Expected User Happiness": h_rating, "Location": location,
                                "Crime Rate": crime, "Host": host_name, "Image_link": img, "Guests":guest, 
                                "Bedrooms": beds, "Bathrooms": bath, "Price($)": h_price, "Review": review})
    
    return recommendations