import tkinter as tk
from tkinter import messagebox
from weather import get_weather

def search_weather():
    city = city_entry.get()
    result = get_weather(city)

    if "error" in result:
        messagebox.showerror("Error", result["error"])
    else:
        output_label.config(
            text=f"""📍 {result['city']}
🌡️ Temperature: {result['temperature']}°C
🌤️ Condition: {result['description']}
💧 Humidity: {result['humidity']}%
🌬️ Wind: {result['wind_speed']} m/s"""
        )

# GUI setup
root = tk.Tk()
root.title("🌦️ Weather App")
root.geometry("350x300")
root.resizable(False, False)

tk.Label(root, text="Enter City Name:", font=("Arial", 12)).pack(pady=10)
city_entry = tk.Entry(root, width=30, font=("Arial", 12))
city_entry.pack()

tk.Button(root, text="Search", font=("Arial", 12), command=search_weather).pack(pady=10)

output_label = tk.Label(root, text="", font=("Arial", 11), justify="left")
output_label.pack(pady=10)

root.mainloop()
