import requests
import sqlite3

# the api key should not be kept publically, should be held in the secrets file
# technically the same could be said about the base url. It lets the attacker know what api you are using


API_KEY = "VEhpcyBpcyBhIGZha2Uga2V5LCBidXQgbWF5YmUgbG9va3MgbGlrZSBvbmU="
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
DB = None

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
    }

    response = requests.get(BASE_URL, params=params)

    #collect from 3rd party API
    #the third party NEEDS to be verified, secure handshake(encryption method)
    data = response.json()

    #a seperate file should be made for retrieving location data
    #allows the seperation of components to prevent everything from becoming compromised
    
    city_name = data["name"]
    temp = data["main"]["temp"]

    #insert into DB
    #THE SQL SHOULD NOT BE HARD CODED HERE
    #a different function should be used
    # additionally, parsing the sql and ensuring all data entries are sanitized is important
    c = DB.cursor()
    c.execute("INSERT INTO history (city, temp) VALUES (" + city_name +", " + temp + ")")
    DB.commit()

    print(f"\nWeather in " + city)
    print(f"Temperature: {temp}°C")
    
    #not secure verification to approve database connection
    # something like cookies that require verification the user is logged into the account
    #with an active session
if __name__ == "__main__":
    DB = sqlite3.connect("weather.db")
    
    #not sanitized
    #not being collected with a safety measure like _POST in php
    #collect from user
    city = input("Enter city name: ")
    get_weather(city)