import requests
import sqlite3

#dont have the api key hardcoded
API_KEY = "VEhpcyBpcyBhIGZha2Uga2V5LCBidXQgbWF5YmUgbG9va3MgbGlrZSBvbmU="
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
DB = None

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
    }

    response = requests.get(BASE_URL, params=params)

    #dont trust 3rd parties without confirming its safe
    #collect from 3rd party API
    data = response.json()
    
    city_name = data["name"]
    temp = data["main"]["temp"]

    #would be better to use a prarmeterized query, also maybe keep in a seperate fille
    #insert into DB
    c = DB.cursor()
    c.execute("INSERT INTO history (city, temp) VALUES (" + city_name +", " + temp + ")")
    DB.commit()

    print(f"\nWeather in " + city)
    print(f"Temperature: {temp}°C")
    
if __name__ == "__main__":
    DB = sqlite3.connect("weather.db")
    
    #no validation? use white listing to make sure theres only valid input
    #collect from user
    city = input("Enter city name: ")
    get_weather(city)