import requests
import sqlite3

# vulnerability 2 - hardcoded/public api key
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
    # vulnerability 3 - not validating api info (api could have been compromised.)
    data = response.json()
    
    city_name = data["name"]
    temp = data["main"]["temp"]

    #insert into DB
    # vulnerability 4 - not utilizing a prepare statement (possible sqli)
    c = DB.cursor()
    # vulnerability 5 (depends on the situation) - not hashing values inside of the database
    c.execute("INSERT INTO history (city, temp) VALUES (" + city_name +", " + temp + ")")
    DB.commit()

    print(f"\nWeather in " + city)
    print(f"Temperature: {temp}°C")
    
if __name__ == "__main__":
    DB = sqlite3.connect("weather.db")
    
    #collect from user
    city = input("Enter city name: ")
    get_weather(city)

    # vulnerability 1 - not validating user input
