from torch import nn
import torch 

class Recommender(nn.Module):

  # Initializing our Neural Network
  def __init__(self, user, location, hotel, hotelrating, price):

    super(Recommender, self).__init__() # Accessing the 'nn' super class

    self.user_em = nn.Embedding(user, 32)
    self.location_em = nn.Embedding(location, 32)
    self.hotel_em = nn.Embedding(hotel, 32)
    self.hotelRating_em = nn.Embedding(hotelrating, 32)
    self.price_em = nn.Embedding(price, 32)

    self.out = nn.Sequential (

        nn.Linear(160, 1)

    )

  # Defining Forward Propogation Function
  def forward(self, user, location, hotel, hotelrating, price):

    users = self.user_em(user)
    loc = self.location_em(location)
    hotel = self.hotel_em(hotel)
    rate = self.hotelRating_em(hotelrating)
    price = self.price_em(price)

    representation_vector = torch.cat([users, loc, hotel, rate, price], 1)
    output = self.out(representation_vector)

    return output
  