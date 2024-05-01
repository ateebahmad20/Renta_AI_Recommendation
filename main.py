from fastapi import FastAPI
from TouristRecommendation.tourist_recommendation import hotel_recommendations
from TenantRecommendation.tenant_recommendation import house_recommendation

app = FastAPI()

@app.get('/')
def home():
    return {"Health Check": "OK", "RENTA Version": "0.0.1"}

@app.post("/House_Recommendation")
def house_recommender(Preferred_Location_1: str, Preferred_Location_2: str, Preferred_Location_3: str, Price_in_k: int):
    houses = house_recommendation(Preferred_Location_1, Preferred_Location_2, Preferred_Location_3, Price_in_k)
    return houses

@app.post('/Hotel_recommendation')
def hotel_recommender(Name: str, Location: str, Price: int):
    hotel = hotel_recommendations(Name, Location, Price)
    return hotel

