import pandas as pd

df = pd.read_csv('TouristRecommendation/TouristDataset.csv')

df_unique_hotels = df.drop_duplicates(subset=['hotel'])
df_unique_hotels = df_unique_hotels.reset_index(drop=True)
df_unique_user = df.drop_duplicates(subset=['userName'])
df_unique_city = df.drop_duplicates(subset=['userCity'])
df_unique_price = df.drop_duplicates(subset=['price_per_night($)'])
df_unique_hotelrating = df.drop_duplicates(subset=['Hotel_rating'])

user_dict = {label:id for id,label in enumerate(df_unique_user.userName)}
hotel_dict = {label:id for id,label in enumerate(df_unique_hotels.hotel)}
reverse_hotel_dict = {id:label for id,label in enumerate(df_unique_hotels.hotel)}
city_dict = {label:id for id,label in enumerate(df_unique_city.userCity)}
price_dict = {label:id for id, label in enumerate(df_unique_price['price_per_night($)'])}
hotelRating_dict = {label:id for id,label in enumerate(df_unique_hotelrating.Hotel_rating)}
Reverse_hotelRating_dict = {id:label for id,label in enumerate(df_unique_hotelrating.Hotel_rating)}

user_classes = df['userid'].max() + 1
hotel_classes = df['hotel_id'].max() + 1
location_classes = df['locationid'].max() + 1
hotelRating_classes = df['Hotel_ratingid'].max() + 1
price_classes = df['price_id'].max() + 1