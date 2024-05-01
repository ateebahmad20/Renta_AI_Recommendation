from fastapi import FastAPI
from TouristRecommendation.tourist_recommendation import *
from TenantRecommendation.tenant_recommendation import house_recommendation

app = FastAPI()

@app.get('/')
def home():
    return {"Health Check": "OK", "RENTA Version": "0.0.1"}

@app.get("/Search_Hotel")
def search_hotel(Hotel_Name: str):
    hotels = get_hotel(Hotel_Name.lower())
    return hotels

@app.get("/Search_Hotel_by_CrimeRate")
def search_hotel_crime(Crime_Rate: str):
    hotels = get_hotel_by_CrimeRate(Crime_Rate.lower())
    return hotels

@app.get("/Search_Hotel_by_location")
def search_hotel_location(Location: str):
    hotels = get_hotel_by_location(Location.lower())
    return hotels

@app.get("/Search_Hotel_by_price")
def search_hotel_price(Max_Price: int):
    hotels = get_hotel_by_price(Max_Price)
    return hotels

@app.post("/House_Recommendation")
def house_recommender(Preferred_Location_1: str, Preferred_Location_2: str, Preferred_Location_3: str, Price_in_k: int):
    houses = house_recommendation(Preferred_Location_1, Preferred_Location_2, Preferred_Location_3, Price_in_k)
    return houses

@app.post('/Hotel_recommendation')
def hotel_recommender(Name: str, Location: str, Price: int):
    hotel = hotel_recommendations(Name, Location, Price)
    return hotel

