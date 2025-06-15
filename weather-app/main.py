from weather import get_weather

def main():
    print("🌦️  Welcome to the Weather App")

    while True:
        city = input("\nEnter a city name (or 'exit' to quit): ").strip()
        if city.lower() == "exit":
            print("👋 Goodbye!")
            break

        data = get_weather(city)
        if data:
            print(f"\n📍 City: {data['city']}")
            print(f"🌡️  Temperature: {data['temperature']}°C")
            print(f"🌤️  Condition: {data['description']}")
            print(f"💧 Humidity: {data['humidity']}%")
            print(f"🌬️  Wind Speed: {data['wind_speed']} m/s")

if __name__ == "__main__":
    main()
