"""
Program Purpose        : Interact with the OpenWeatherMap API to get weather forecasts by US Zip Code or US City.
Author                 : Kapambwe Chulu
Original Creation date : 2/22/2023
"""

import requests


def print_weather_data(city_name, current_temperature, high_temperature, low_temperature, pressure, humidity, cloud_cover, description):
    # This function is used to print the weather forecast  to the screen.
    # The chr function in the print statements outputs the degree symbol.
    print(' ')
    print(' '*3, 'Current Weather Condition for ', city_name)
    print('Current Temperature : ', current_temperature, chr(176))
    print('Highest Temperature : ', high_temperature, chr(176))
    print('Lowest Temperature  : ', low_temperature, chr(176))
    print('Pressure            : ', pressure, "hPa")
    print('Humidity            : ', humidity, chr(37))
    print('Cloud Cover         : ', cloud_cover)
    print('Description         : ', description)
    print(' ')


def extract_weather_condition(temperature_data):
    # This function extracts city name and the weather conditions of the city.
    temperature_data_json = temperature_data.json()
    city_name = temperature_data_json['name']
    current_temperature = temperature_data_json['main']['temp']
    high_temperature = temperature_data_json['main']['temp_max']
    low_temperature = temperature_data_json['main']['temp_min']
    pressure = temperature_data_json['main']['pressure']
    humidity = temperature_data_json['main']['humidity']
    cloud_cover = temperature_data_json['weather'][0]['main']
    description = temperature_data_json['weather'][0]['description']
    print_weather_data(city_name, current_temperature, high_temperature, low_temperature, pressure, humidity, cloud_cover, description)


def fahrenheit(longitude, latitude, api_key):
    # This function requests the weather forecast from the webservice in fahrenheit.
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&APPId={api_key}&units=imperial"
    try:
        temperature_data = requests.get(url)
        temperature_data.raise_for_status()
    except requests.exceptions.HTTPError:
        print("Http Error:Sorry, connection to the webservice was not successful. Please try again")
    except requests.exceptions.ConnectionError:
        print(" " * 3, "Connection Error: Sorry, please ensure that you are connected to the internet and try again.")
    else:
        print(" "*3, "Note(2): The second connection to the webservice was successful.")
        extract_weather_condition(temperature_data)


def celsius(longitude, latitude, api_key):
    # This function requests the weather forecast from the webservice in Celsius.
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&APPId={api_key}&units=metric"
    try:
        temperature_data = requests.get(url)
        temperature_data.raise_for_status()
    except requests.exceptions.HTTPError:
        print("Http Error:Sorry, Latitude/Longitude to the webservice was not successful. Please try again")
    except requests.exceptions.ConnectionError:
        print(" " * 3, "Connection Error: Sorry, please ensure that you are connected to the internet and try again.")
    else:
        print(" "*3, "Note(2): The Latitude/Longitude connection to the webservice was successful.")
        extract_weather_condition(temperature_data)


def kelvin(longitude, latitude, api_key):
    # This function requests the weather forecast from the webservice in Kelvin.
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&APPId={api_key}"
    try:
        temperature_data = requests.get(url)
        temperature_data.raise_for_status()
    except requests.exceptions.HTTPError:
        print("Http Error:Sorry, connection to the webservice was not successful. Please try again")
    except requests.exceptions.ConnectionError:
        print(" " * 3, "Connection Error: Sorry, please ensure that you are connected to the internet and try again.")
    else:
        print(" "*3, "Note(2): The Latitude/Longitude connection to the webservice was successful.")
        extract_weather_condition(temperature_data)


def weather(weather_data,  api_key):
    # This function extracts latitude and longitude from the Geo Lookup, and uses them to extract weather data.
    weather_data_json = weather_data.json()
    longitude = weather_data_json['coord']['lon']
    latitude = weather_data_json['coord']['lat']
    temperature_unit = 0
    while temperature_unit != 'Q':
        print('Would you like to view temperature in Fahrenheit, Celsius or Kelvin?')
        temperature_unit = input('Please enter F for Fahrenheit, C for Celsius, K for Kelvin or Q to Quit: ').upper()
        if temperature_unit == 'Q':
            print(" "*3, "You entered Q to Quit. Just to confirm:")
            break
        elif temperature_unit == 'F':
            fahrenheit(longitude, latitude, api_key)
            break
        elif temperature_unit == 'C':
            celsius(longitude, latitude, api_key)
            break
        elif temperature_unit == 'K':
            kelvin(longitude, latitude, api_key)
            break
        else:
            print(" "*3, "Sorry, You entered an invalid value for temperature units. Please try again.")


def zipcode_lookup(api_key):
    # This function does a Geo Lookup by zip code.
    zip_code = 0
    while zip_code != 'Q':
        zip_code = input('Please enter a  valid 5-digit US zip code, or Q to Quit:  ').upper()
        if zip_code == 'Q':
            print(" "*3, "You entered Q to Quit. Just to confirm: ")
            break
        else:
            try:
                url = f"https://api.openweathermap.org/data/2.5/weather?zip={zip_code},us&APPId={api_key}"
                weather_data = requests.get(url)
                weather_data.raise_for_status()
            except requests.exceptions.HTTPError:
                print(" ")
                print(" "*3, "Http Error:Sorry, you entered an invalid US zip code.")
                print("For zip code you entered : ", zip_code)
                print(" ")
            except requests.exceptions.ConnectionError:
                print(" " * 3, "Connection Error: Sorry, please ensure that you are connected to the internet and try again.")
            else:
                print(" ")
                print(" "*3, "Note(1):The zip code connection to the webservice was successful.")
                weather(weather_data, api_key)
                break


def city_lookup(api_key):
    # This function does a Geo Lookup by City/State
    city_name = 0
    state = 0
    while city_name != 'Q' and state != 'NA':
        city_name = input('Please enter a valid City Name or Q to Quit: ').upper()
        state = input('Please enter a valid state abbreviation or NA if you entered Q to Quit for city name: ').upper()
        if city_name == 'Q' and state == 'NA':
            print(" "*3, " You enter Q for city to Quit. Just to confirm: ")
            break
        else:
            try:
                url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name},{state},us&APPid={api_key}"
                weather_data = requests.get(url)
                weather_data.raise_for_status()
            except requests.exceptions.HTTPError:
                print(" " * 3, "Http Error:Sorry, your City name or state abbreviation maybe invalid.")
                print("For city name you entered : ", city_name)
                print("For state abbreviation you entered : ", state)
                print(" ")
            except requests.exceptions.ConnectionError:
                print(" "*3, "Connection Error: Sorry, please ensure that you are connected to the internet and try again.")
            else:
                print(" ")
                print(" " * 3, "Note(1): The city/state connection to the webservice was successful.")
                weather(weather_data, api_key)
                break


def inquiry():
    # This function asks the user if they want to request whether by US zip code or US city.
    zip_or_city = 0
    while zip_or_city != '3':
        api_key = 'Enter API key'
        zip_or_city = input('Would you like to lookup the weather by Zip Code or US City? Enter 1 for Zip Code,2 for City, or 3 to Quit: ')
        if zip_or_city == '3':
            print(" "*3, "You entered 3 to Quit. Just to confirm: ")
            break
        elif zip_or_city == '1':
            zipcode_lookup(api_key)
            break
        elif zip_or_city == '2':
            city_lookup(api_key)
            break
        else:
            print('Sorry you entered an invalid option. Please try again.')


def main():
    # The main function calls all the other functions in order to generate the weather forecasts.
    print(" ")
    print('****************************** Welcome to the Weather Forecast App ***************************************************')
    print(' ')
    lookup = 0
    while lookup != 'N':
        inquiry()
        lookup = input('Would you like to perform another weather lookup? Enter Y for Yes, or N for No: ').upper()
        if lookup == 'N':
            print('Thank you for using the Weather Forecast App. Hope you have a nice day.')
            break
        elif lookup == 'Y':
            continue
        else:
            print('Sorry , You entered an invalid value')


if __name__ == '__main__':
    main()
else:
    # The statements below will execute if this program is imported to another module.
    print(" Note: You are using functions which were created in another module. ")
