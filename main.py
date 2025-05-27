import os
import requests

def fetch_weather(city):
    api_key =bdf5a4056376bfd95284755824ba216a
    if not api_key:
        raise ValueError("No API key found in environment variable MY_API_KEY")

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temperature = data["main"]["temp"]
        print(f"Current temperature in {city}: {temperature}°C")
    else:
        print("Failed to fetch weather data.")
        print("Status Code:", response.status_code)
        print("Response:", response.text)

if __name__ == "__main__":
    fetch_weather("Edmonton")
