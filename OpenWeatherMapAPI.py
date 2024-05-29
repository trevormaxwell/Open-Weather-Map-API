# Change #1
# Changes Made: initial base code
# Date of Change: 2/15/2022
# Author: Trevor Maxwell
# Change Approved By: Professor Michael Eller
# Date Moved to Production: 3/04/2023

import json
import requests


def get_temperature_city_state(lat, lon, units):
    """function used to receive temperature using city/state API call"""

    # defining API Key and URL
    API_key = "your_API_key_here"
    url_temp = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units={units}"

    # try block to connect to API, if error occurs then display error and quit program. If successful, retrieve data from API
    try:
        temp_dict = requests.get(url_temp)

    except requests.exceptions.RequestException:
        print(f"\nA connection error occurred. Please try again later.")
        quit()

    else:
        temp_dict = temp_dict.text
        temp_dict_txt = json.loads(temp_dict)

        # List created to obtain multiple descriptions for current weather if applicable
        weather_list = []
        for item in temp_dict_txt['weather']:
            for weather_type in item:
                if weather_type == 'description':
                    weather_list.append(item[weather_type])
        delimiter = '/'
        weather_desc = delimiter.join(weather_list)

        # Obtain weather data from API
        current_temp = round(temp_dict_txt["main"]["temp"])
        feels_temp = round(temp_dict_txt["main"]["feels_like"])
        min_temp = round(temp_dict_txt["main"]["temp_min"])
        max_temp = round(temp_dict_txt["main"]["temp_max"])
        humidity = round(temp_dict_txt["main"]["humidity"])
        pressure = round(temp_dict_txt["main"]["pressure"])

        return weather_desc, current_temp, feels_temp, min_temp, max_temp, humidity, pressure


def get_temperature_zip_code(lat, lon, units):
    """function used to receive temperature using zip code API call"""

    # defining API Key and URL
    API_key = "your_API_key_here"
    url_temp = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units={units}"

    # try block to connect to API, if error occurs then display error and quit program. If successful, retrieve data from API
    try:
        temp_dict = requests.get(url_temp)

    except requests.exceptions.RequestException:
        print(f"\nA connection error occurred. Please try again later.")
        quit()

    else:
        temp_dict = temp_dict.text
        temp_dict_txt = json.loads(temp_dict)

        # List created to obtain multiple descriptions for current weather if applicable
        weather_list = []
        for item in temp_dict_txt['weather']:
            for weather_type in item:
                if weather_type == 'description':
                    weather_list.append(item[weather_type])
        delimiter = '/'
        weather_desc = delimiter.join(weather_list)

        # Obtain weather data from API
        current_temp = round(temp_dict_txt["main"]["temp"])
        feels_temp = round(temp_dict_txt["main"]["feels_like"])
        min_temp = round(temp_dict_txt["main"]["temp_min"])
        max_temp = round(temp_dict_txt["main"]["temp_max"])
        humidity = round(temp_dict_txt["main"]["humidity"])
        pressure = round(temp_dict_txt["main"]["pressure"])

        return weather_desc, current_temp, feels_temp, min_temp, max_temp, humidity, pressure


def get_coordinates_city_state(city, state, units):
    """function to obtain latitude and longitude from API using City/State"""

    # defining API Key and URL
    API_key = "your_API_key_here"
    url_city = f"http://api.openweathermap.org/geo/1.0/direct?q={city},{state},&appid={API_key}"

    # GET request to obtain lat and lon of inputted city
    try:

        temp_dict = requests.get(url_city)

    except requests.exceptions.RequestException:
        print(f"\nA connection error occurred. Please try again later.")
        quit()

    # Convert return format from API to text and the retrieve lat and lon
    temp_dict = temp_dict.text
    temp_dict_txt = json.loads(temp_dict)

    # if connection to API is successful but does not yield results, return error message
    if temp_dict_txt == []:

        err = f"\nCity/State '{city.capitalize()}, {state.upper()}' did not yield results.\nPlease try again."
        return err

    else:

        # Obtain lat and lon from API and input into get_temperature_zip_code() function to get weather details
        for coordinates in temp_dict_txt:
            lat = coordinates['lat']
            lon = coordinates['lon']

        weather_desc, current_temp, feels_temp, min_temp, max_temp, humidity, pressure = get_temperature_city_state(lat, lon, units)

        return weather_desc, current_temp, feels_temp, min_temp, max_temp, humidity, pressure


def get_coordinates_zip_code(zip_code, units):
    """function to obtain latitude and longitude from API using zip code"""

    # defining API Key and URL
    API_key = "your_API_key_here"
    url_zip = f"https://api.openweathermap.org/data/2.5/weather?zip={zip_code},&appid={API_key}"

    # GET request to obtain lat and lon of inputted zip code, if error then quit
    try:

        temp_dict = requests.get(url_zip)

    except requests.exceptions.RequestException:
        print(f"\nA connection error occurred. Please try again later.")
        quit()

    else:
        temp_dict = temp_dict.text
        temp_dict_txt = json.loads(temp_dict)

        # if connection to API is successful but does not yield results, return error message
        if temp_dict_txt["cod"] == '404':
            err = f"\nZip Code '{zip_code}' did not yield results.\nPlease try again."
            return err

        else:

            # Obtain lat and lon from API and input into get_temperature_zip_code() function to get weather details
            lat = str(temp_dict_txt["coord"]["lat"])
            lon = str(temp_dict_txt["coord"]["lon"])

            weather_desc, current_temp, feels_temp, min_temp, max_temp, humidity, pressure = get_temperature_zip_code(lat, lon, units)

            return weather_desc, current_temp, feels_temp, min_temp, max_temp, humidity, pressure


def main():
    """defining main() method to handle receiving inputs from user and displaying weather report"""

    print("Welcome to the Weather Report Generator!")

    sentinel = 'QUIT'

    while True:
        # Request type of weather report from user or quit if sentinel value is entered
        city_or_zip = input("\nEnter 'city' for City/State lookup, 'zip' for Zip Code lookup, or 'quit' to exit: ")

        if city_or_zip.upper().strip() == sentinel:
            print("\nThank you for using the Weather Report Generator!")
            quit()

        while True:

            # Request units from user or quit if sentinel value is entered
            unit_indicator = input("\nPlease enter 'F' for Fahrenheit, 'C' for Celsius,'K' for Kelvin or 'quit' to exit: ")

            if unit_indicator.upper().strip() == 'C':
                units = 'metric'
                break

            elif unit_indicator.upper().strip() == 'F':
                units = 'imperial'
                break

            elif unit_indicator.upper().strip() == 'K':
                units = 'standard'
                break

            elif unit_indicator.upper().strip() == sentinel:
                print("\nThank you for using the Weather Report Generator!")
                quit()

            else:
                print(f"\n'{unit_indicator}' is not a valid input for temperature units.")
                continue

        # loop if a City/State request is entered
        if city_or_zip.upper().strip() == 'CITY':

            while True:

                city = str(input("\nEnter the city name (or 'quit' to exit): "))

                if city.upper().strip() == sentinel:
                    print("\nThank you for using the Weather Report Generator!")
                    quit()

                state = str(input("\nEnter the state abbreviation (or 'quit' to exit): "))

                if state.upper().strip() == sentinel:
                    print("\nThank you for using the Weather Report Generator!")
                    quit()

                try:
                    # Retrieve weather report values from get_coordinates_city_state() function
                    weather_desc, current_temp, feels_temp, min_temp, max_temp, humidity, pressure = get_coordinates_city_state(city, state, units)

                # If error occurs, display error message
                except ValueError:
                    err = get_coordinates_city_state(city, state, units)
                    print(err)

                except TypeError:
                    err = get_coordinates_city_state(city, state, units)
                    print(err)

                except:
                    print(f"An error has occurred. Please try again.")

                else:

                    # Print weather report if successful
                    print(f"\nWeather Report for Zip Code {city.capitalize()}, {state.upper()}")
                    print("-" * 35)
                    print(f"Current weather:{chr(32)*(6)}{weather_desc}")

                    if units == 'imperial':
                        print(f"Current temperature:{chr(32) * 2}{current_temp}{chr(176)}F")
                        print(f"Feels like:{chr(32) * 11}{feels_temp}{chr(176)}F")
                        print(f"Minimum temperature:{chr(32) * 2}{min_temp}{chr(176)}F")
                        print(f"Maximum temperature:{chr(32) * 2}{max_temp}{chr(176)}F")
                        print(f"Humidity Level:{chr(32) * 7}{humidity}%")
                        print(f"Pressure:{chr(32) * 13}{pressure} hPa")
                        break

                    elif units == 'metric':
                        print(f"Current temperature:{chr(32) * 2}{current_temp}{chr(176)}C")
                        print(f"Feels like:{chr(32) * 11}{feels_temp}{chr(176)}C")
                        print(f"Minimum temperature:{chr(32) * 2}{min_temp}{chr(176)}C")
                        print(f"Maximum temperature:{chr(32) * 2}{max_temp}{chr(176)}C")
                        print(f"Humidity Level:{chr(32) * 7}{humidity}%")
                        print(f"Pressure:{chr(32) * 13}{pressure} hPa")
                        break

                    elif units == 'standard':
                        print(f"Current temperature:{chr(32) * 2}{current_temp} K")
                        print(f"Feels like:{chr(32) * 11}{feels_temp} k")
                        print(f"Minimum temperature:{chr(32) * 2}{min_temp} K")
                        print(f"Maximum temperature:{chr(32) * 2}{max_temp} K")
                        print(f"Humidity Level:{chr(32) * 7}{humidity}%")
                        print(f"Pressure:{chr(32) * 13}{pressure} hPa")
                        break

        # loop if zip code request is entered
        elif city_or_zip.upper().strip() == 'ZIP':

            while True:
                zip_code = str(input("\nEnter the Zip Code for Weather Report (or 'quit' to exit): "))

                if zip_code.upper().strip() == sentinel:
                    print("\nThank you for using the Weather Report Generator!")
                    quit()

                try:
                    # Retrieve weather report values from get_coordinates_zip_code() function
                    weather_desc, current_temp, feels_temp, min_temp, max_temp, humidity, pressure = get_coordinates_zip_code(zip_code, units)

                # If error occurs, display error message
                except ValueError:
                    err = get_coordinates_zip_code(zip_code, units)
                    print(err)

                except TypeError:
                    err = get_coordinates_zip_code(zip_code, units)
                    print(err)

                    break

                else:

                    # Print weather report if successful
                    print(f"\nWeather Report for Zip Code {zip_code}")
                    print("-" * 35)
                    print(f"Current weather:{chr(32)*(6)}{weather_desc}")

                    if units == 'imperial':
                        print(f"Current temperature:{chr(32) * 2}{current_temp}{chr(176)}F")
                        print(f"Feels like:{chr(32) * 11}{feels_temp}{chr(176)}F")
                        print(f"Minimum temperature:{chr(32) * 2}{min_temp}{chr(176)}F")
                        print(f"Maximum temperature:{chr(32) * 2}{max_temp}{chr(176)}F")
                        print(f"Humidity Level:{chr(32) * 7}{humidity}%")
                        print(f"Pressure:{chr(32) * 13}{pressure} hPa")
                        break

                    elif units == 'metric':
                        print(f"Current temperature:{chr(32) * 2}{current_temp}{chr(176)}C")
                        print(f"Feels like:{chr(32) * 11}{feels_temp}{chr(176)}C")
                        print(f"Minimum temperature:{chr(32) * 2}{min_temp}{chr(176)}C")
                        print(f"Maximum temperature:{chr(32) * 2}{max_temp}{chr(176)}C")
                        print(f"Humidity Level:{chr(32) * 7}{humidity}%")
                        print(f"Pressure:{chr(32) * 13}{pressure} hPa")
                        break

                    elif units == 'standard':
                        print(f"Current temperature:{chr(32) * 2}{current_temp} K")
                        print(f"Feels like:{chr(32) * 11}{feels_temp} k")
                        print(f"Minimum temperature:{chr(32) * 2}{min_temp} K")
                        print(f"Maximum temperature:{chr(32) * 2}{max_temp} K")
                        print(f"Humidity Level:{chr(32) * 7}{humidity}%")
                        print(f"Pressure:{chr(32) * 13}{pressure} hPa")
                        break

        else:
            print(f"\n'{city_or_zip}' is not an acceptable input for a weather report lookup.")
            continue

        # loop to ask if another request is needed
        while True:

            next_temp = input("\nWould you like to generate another weather report? (Enter 'Y' for yes, 'N' for no): ")

            if next_temp.upper().strip() == 'Y':
                break
            elif next_temp.upper().strip() == 'N':
                print('\nThank you for using the Weather Report Generator!')
                quit()
            else:
                print(f"\n'{next_temp}' is not a valid input.")
                continue


if __name__ == '__main__':
    main()
else:
    print("Run Current Weather Report in final_project Program")

