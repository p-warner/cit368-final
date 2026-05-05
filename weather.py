import requests
import sqlite3

#Hard coded API KEY / encoding base64
API_KEY = "VEhpcyBpcyBhIGZha2Uga2V5LCBidXQgbWF5YmUgbG9va3MgbGlrZSBvbmU="
# insecure http "s"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
#unsafe
DB = None

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
    }
 
    response = requests.get(BASE_URL, params=params)

    #collect from 3rd party API
    # no error handling for 
    data = response.json()
    
    city_name = data["name"]
    temp = data["main"]["temp"]

    #insert into DB 
    # no error handling
    c = DB.cursor()
    # SQL injection
    c.execute("INSERT INTO history (city, temp) VALUES (" + city_name +", " + temp + ")")
    DB.commit()

    print(f"\nWeather in " + city)
    print(f"Temperature: {temp}°C")
    
if __name__ == "__main__":
    DB = sqlite3.connect("weather.db")
    
    #collect from user
    # missing input validation
    city = input("Enter city name: ")
    get_weather(city)