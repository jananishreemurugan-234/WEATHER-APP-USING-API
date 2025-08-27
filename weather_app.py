import requests
import tkinter as tk
from tkinter import messagebox

# ---- Replace with your OpenWeatherMap API Key ----
API_KEY = "611038c4efa6f8681dd21db9e5609020"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather():
    city = city_entry.get()
    if city == "":
        messagebox.showwarning("Input Error", "Please enter a city name")
        return

    # Build URL
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()
       
        if data["cod"] == 200:
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            description = data["weather"][0]["description"].capitalize()
           
            result_label.config(text=f"Temperature: {temp}°C\n"
                                     f"Humidity: {humidity}%\n"
                                     f"Description: {description}")
        else:
            messagebox.showerror("Error", f"City '{city}' not found!")
            result_label.config(text="")
    except Exception as e:
        messagebox.showerror("Error", "Failed to retrieve data.\nCheck your internet connection.")
        result_label.config(text="")

# ---- Tkinter UI ----
root = tk.Tk()
root.title("Weather App")
root.geometry("300x250")
root.resizable(False, False)

title_label = tk.Label(root, text="Weather App", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

city_entry = tk.Entry(root, font=("Arial", 14), justify="center")
city_entry.pack(pady=10)
city_entry.insert(0, "Enter city name")

get_btn = tk.Button(root, text="Get Weather", font=("Arial", 12), command=get_weather)
get_btn.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
result_label.pack(pady=20)

root.mainloop()