import requests # possible supply chain vulnerability
import sqlite3  # possible supply chain vulnerability

API_KEY = "VEhpcyBpcyBhIGZha2Uga2V5LCBidXQgbWF5YmUgbG9va3MgbGlrZSBvbmU="    #hardcoded API key, either put in private file or env var
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
DB = None

def get_weather(city):
    params = {
        "q": city,  # this looks like it could even be used to attack openweathermap, since nonvalidated input is being used as parameters for API call
        "appid": API_KEY,
    }

    response = requests.get(BASE_URL, params=params)    

    #collect from 3rd party API
    data = response.json()      # maybe validate API reponse, is a trusted source but looks like error from openweathermap could lead to some kind of injection

    city_name = data["name"]
    temp = data["main"]["temp"]

    #insert into DB
    c = DB.cursor()
    c.execute("INSERT INTO history (city, temp) VALUES (" + city_name +", " + temp + ")")       # inserting possibly compromised input, SQLi
    DB.commit() 

    print(f"\nWeather in " + city)
    print(f"Temperature: {temp}°C")
    
if __name__ == "__main__":
    DB = sqlite3.connect("weather.db")
    
    #collect from user
    city = input("Enter city name: ")   # 0 input validation, should at least add some regex or other whitelist
    get_weather(city)   # function call to openweatherapi with possibly compromised input