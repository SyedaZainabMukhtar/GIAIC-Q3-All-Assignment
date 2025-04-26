# Requires 'requests': pip install requests
# Get API key from https://openweathermap.org/api
import requests

def get_weather():
    api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
    city = input("Enter city name: ")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()
        if data["cod"] == 200:
            print(f"Weather in {city}:")
            print(f"Temperature: {data['main']['temp']}°C")
            print(f"Description: {data['weather'][0]['description']}")
        else:
            print("City not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print("Get an API key from https://openweathermap.org/api")
    get_weather()