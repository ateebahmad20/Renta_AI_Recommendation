from TouristRecommendation.tourist_dataset import user_dict, city_dict, price_dict

def get_ids(user, location, price):
 
    ### Use Case of Getting Name: ###

    # Convert the user's name to capitalize format
    user_name_capitalized = user.capitalize()

    # Check if the user's name is already in the dictionary
    if user_name_capitalized in user_dict.keys():
        # If the user's name is in the dictionary, retrieve the corresponding ID
        user_id = user_dict[user_name_capitalized]

    else:
        # If the user's name is not in the dictionary, add it with a new ID
        max_id = max(user_dict.values()) if user_dict else 0  # Find the maximum existing ID
        new_id = max_id + 1  # Increment the maximum ID to generate a new ID
        user_dict[user_name_capitalized] = new_id
        user_id = new_id

    ### Use Case of Getting Location: ###

    # Convert the user's name to capitalize format
    location_capitalized = location.capitalize()

    # Check if the user's name is already in the dictionary
    if location_capitalized in city_dict.keys():
        # If the location's name is in the dictionary, retrieve the corresponding ID
        location_id = city_dict[location_capitalized]

    else:
        # If the location's name is not in the dictionary, add it with a new ID
        max_id = max(city_dict.values()) if city_dict else 0  # Find the maximum existing ID
        new_id = max_id + 1  # Increment the maximum ID to generate a new ID
        city_dict[location_capitalized] = new_id
        location_id = new_id

    ### Use Case of Getting Price: ###

    # Check if the user's desired price is in the dictionary
    if price in price_dict.keys():
        # If the price is in the dictionary, retrieve its corresponding ID
        price_id = price_dict[price]

    else:
        print("done")
        # If the price is not in the dictionary, find the closest price and assign its ID
        closest_price = min(price_dict.keys(), key=lambda x: abs(x - price))
        price_id = price_dict[closest_price]
    
    return user_id, location_id, price_id