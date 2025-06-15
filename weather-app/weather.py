import requests
from config import API_KEY

def get_weather(city_name):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params)

        if response.status_code == 401:
            return {"error": "Invalid API key."}

        response.raise_for_status()

        data = response.json()

        return {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"].title(),
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"]
        }

    except requests.exceptions.RequestException:
        print("⚠️ Network issue. Please check your connection.")
        return None
    except KeyError:
        print("❌ Unable to parse weather data for that city.")
        return None
