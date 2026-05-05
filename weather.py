import requests
import sqlite3

# API key not encrypted
API_KEY = "VEhpcyBpcyBhIGZha2Uga2V5LCBidXQgbWF5YmUgbG9va3MgbGlrZSBvbmU="
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
DB = None

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY, #should be stored first
    }

    response = requests.get(BASE_URL, params=params)

    
    #collect from 3rd party API
    data = response.json() 
    
    city_name = data["name"]
    temp = data["main"]["temp"]

    #SQL injection!!!!!!
    #insert into DB
    c = DB.cursor()
    c.execute("INSERT INTO history (city, temp) VALUES (" + city_name +", " + temp + ")")
    DB.commit()

    print(f"\nWeather in " + city) #dont think you need to cat here
    print(f"Temperature: {temp}°C") 
    
if __name__ == "__main__":
    
    DB = sqlite3.connect("weather.db")
    
    #collect from user
    city = input("Enter city name: ") #taken staright from user big error
    get_weather(city)