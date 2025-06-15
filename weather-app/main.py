import tkinter as tk
from tkinter import messagebox
from weather import get_weather

# Choose emoji based on weather type
def get_weather_icon(main_weather):
    icons = {
        "clear": "☀️",
        "clouds": "☁️",
        "rain": "🌧️",
        "drizzle": "🌦️",
        "thunderstorm": "⛈️",
        "snow": "❄️",
        "mist": "🌫️",
        "haze": "🌁",
        "fog": "🌁",
    }
    return icons.get(main_weather.lower(), "🌍")

def search_weather():
    city = city_entry.get()
    result = get_weather(city)

    if "error" in result:
        messagebox.showerror("Error", result["error"])
    else:
        icon = get_weather_icon(result["main_weather"])
        city_label.config(text=f"{icon} {result['city']}", fg="#FFD700")
        temp_label.config(text=f"🌡️ Temp: {result['temperature']}°C", fg="#FF5733")
        desc_label.config(text=f"🌤️ {result['description']}", fg="#33C4FF")
        humidity_label.config(text=f"💧 Humidity: {result['humidity']}%", fg="#00C49A")
        wind_label.config(text=f"🌬️ Wind: {result['wind_speed']} m/s", fg="#A569BD")

# GUI Setup
root = tk.Tk()
root.title("🌦️ Weather App")
root.geometry("360x360")
root.configure(bg="#1E1E1E")
root.resizable(False, False)

# Input section
tk.Label(root, text="Enter City Name", font=("Arial", 13), bg="#1E1E1E", fg="white").pack(pady=(20, 5))
city_entry = tk.Entry(root, font=("Arial", 13), width=25)
city_entry.pack(pady=5)
tk.Button(root, text="Search", font=("Arial", 12), command=search_weather).pack(pady=10)

# Output section
city_label = tk.Label(root, font=("Arial", 16, "bold"), bg="#1E1E1E")
city_label.pack(pady=(20, 5))

temp_label = tk.Label(root, font=("Arial", 13), bg="#1E1E1E")
temp_label.pack()

desc_label = tk.Label(root, font=("Arial", 13), bg="#1E1E1E")
desc_label.pack()

humidity_label = tk.Label(root, font=("Arial", 13), bg="#1E1E1E")
humidity_label.pack()

wind_label = tk.Label(root, font=("Arial", 13), bg="#1E1E1E")
wind_label.pack()

root.mainloop()
