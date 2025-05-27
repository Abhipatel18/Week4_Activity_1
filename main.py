import os
import requests

def fetch_weather(city):
    api_key = os.getenv("WEATHER_API_KEY")
    if not api_key:
        raise ValueError("No API key found in environment variable WEATHER_API_KEY")

    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(f"Current temperature in {city}: {data['current']['temp_c']}°C")
    else:
        print("Failed to fetch weather data.")
        print("Status Code:", response.status_code)
        print("Response:", response.text)

if __name__ == "__main__":
    fetch_weather("Toronto")
