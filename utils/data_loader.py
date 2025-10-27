import os 
import requests # для http запросов
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_URL = os.getenv("API_URL")

def load_data(city):
    response = requests.get(API_URL, params = {'key': API_KEY, 'q': city, 'days': 1, 'aqi': 'yes'})
    data = response.json()
    city_name = data['location']['name'] # название города
    day = data['current']['last_updated'][:10]
    co = data['current']['air_quality']['co']
    no2 = data["current"]["air_quality"]["no2"]
    o3 = data["current"]["air_quality"]["o3"]
    so2 = data["current"]["air_quality"]["so2"]
    pm2_5 = data["current"]["air_quality"]["pm2_5"]
    pm10 = data["current"]["air_quality"]["pm10"]
    us_epa_index = data["current"]["air_quality"]["us-epa-index"]
    gb_defra_index = data["current"]["air_quality"]["gb-defra-index"]

    forecast_day = data["forecast"]["forecastday"][0]["hour"]
    hour = [hour["time"][-5:] for hour in forecast_day]
    co_hour = [hour["air_quality"]["co"] for hour in forecast_day]
    no2_hour = [hour["air_quality"]["no2"] for hour in forecast_day]
    o3_hour = [hour["air_quality"]["o3"] for hour in forecast_day]
    so2_hour = [hour["air_quality"]["so2"] for hour in forecast_day]
    pm2_5_hour = [hour["air_quality"]["pm2_5"] for hour in forecast_day]
    pm10_hour = [hour["air_quality"]["pm10"] for hour in forecast_day]

    return{
        'city_name': city_name,
        'day': day,
        'co': co,
        'no2': no2,
        'o3': o3,
        'so2': so2,
        'pm2_5': pm2_5,
        'pm10': pm10,
        'us_epa_index': us_epa_index,
        'gb_defra_index': gb_defra_index,
        'hour': hour,
        'co_hour': co_hour,
        'no2_hour': no2_hour,
        'o3_hour': o3_hour,
        'so2_hour': so2_hour,
        'pm2_5_hour': pm2_5_hour,
        'pm10_hour':pm10_hour
    }
   