import requests

# Your OpenWeatherMap API key
API_KEY = "YOUR_API_KEY_HERE"

def get_weather(city):
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(base_url)
    
    if response.status_code == 200:
        weather_data = response.json()
        print(f"Weather in {weather_data['name']}:")
        print(f"  Temperature: {weather_data['main']['temp']}°C")
        print(f"  Humidity: {weather_data['main']['humidity']}%")
    else:
        print("Failed to retrieve weather data.")

# Example usage
city = "Kuala Lumpur"
get_weather(city)