# This is a command line tool that will take city name as input and return the weather data.
# The weather data will be fetched from OpenWeatherMap API.

# import requests module to make http requests
import requests

# convert function to a command line tool using argparse
import argparse


def call_api(city):
    # fetch the key from a config file
    import configparser
    config = configparser.ConfigParser()
    config.read('config.ini')
    api_key = config['openweathermap']['api_key']
    # api_key = "159889a6b37cf9a30ddbdc10edf27cdb"
    base_url = config['openweathermap']['base_url']
    # base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city
    response_from_api = requests.get(complete_url)
    return response_from_api.json()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("city", help="City name to get weather data")
    args = parser.parse_args()
    # check if city is passed as argument
    if args.city is None:
        print("Please provide city name")
        exit(1)

    response = call_api(args.city)
    # check if valid city name is passed
    if response['cod'] != 200:
        print("Invalid city name")
        exit(1)
    # get the weather from the response
    weather = response['weather'][0]['description']
    print(weather)

