import os
import requests
from dotenv import load_dotenv
import argparse



class WeatherFetcher:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("OPENWEATHERMAP_API_KEY")
        if not self.api_key:
            raise ValueError("OpenWeatherMap API key not found. Please set it in your .env file.")
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"

    def get_current_weather(self, city: str) -> str:
        """
        Fetches the current weather for a given city.

        Args:
            city: The name of the city.

        Returns:
            A string describing the current weather, or an error message.
        """
        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric"  # Use "imperial" for Fahrenheit
        }
        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()  # Raises an exception for bad status codes (4xx or 5xx)
            data = response.json()
            
            # Extracting relevant information
            weather_desc = data['weather'][0]['description']
            temp = data['main']['temp']
            feels_like = data['main']['feels_like']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']

            return (
                f"The current weather in {city.title()} is {weather_desc} "
                f"with a temperature of {temp}°C (feels like {feels_like}°C). "
                f"Humidity is at {humidity}% and wind speed is {wind_speed} m/s."
            )

        except requests.exceptions.RequestException as e:
            if e.response and e.response.status_code == 404:
                return f"Sorry, I couldn't find the city '{city}'. Please check the spelling."
            return f"An error occurred while fetching weather data: {e}"
        except KeyError:
            return "Sorry, there was an issue processing the weather data."

if __name__ == '__main__':
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="Test the WeatherFetcher tool by providing a city name.")
    parser.add_argument(
        "city", 
        nargs='?', 
        default="London", 
        help="The name of the city to test (e.g., 'Paris'). Defaults to 'London' if not provided."
    )
    args = parser.parse_args()

    # This is for testing the tool directly
    weather_tool = WeatherFetcher()
    city_to_test = args.city
    
    print(f"--- Testing Weather Tool for '{city_to_test}' ---")
    weather_report = weather_tool.get_current_weather(city_to_test)
    print(weather_report)
    print("-" * 20)
    print("You can test another city by running: python travel_agent/tools.py \"New York\"")

