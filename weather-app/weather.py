import requests
from config import API_KEY

def get_weather(city_name):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": "metric"  # use "imperial" for °F
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise error for bad status

        data = response.json()
        weather_data = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"].title(),
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"]
        }
        return weather_data
    except requests.RequestException as e:
        print("🔌 Network error:", e)
    except KeyError:
        print("❌ Could not find weather data for that city.")
