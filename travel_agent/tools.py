# ... existing code ...
        except KeyError:
            return "Sorry, there was an issue processing the weather data."

if __name__ == '__main__':
    import argparse

    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="Test the WeatherFetcher tool by providing a city name.")
    parser.add_argument("city", nargs='?', default="London", help="The name of the city to test (e.g., 'Paris'). Defaults to 'London' if not provided.")
    args = parser.parse_args()

    # This is for testing the tool directly
    weather_tool = WeatherFetcher()
    city_to_test = args.city
    
    print(f"--- Testing Weather Tool for '{city_to_test}' ---")
    weather_report = weather_tool.get_current_weather(city_to_test)
    print(weather_report)
    print("-" * 20)
    print("You can test another city by running: python travel_agent/tools.py 'New York'") 