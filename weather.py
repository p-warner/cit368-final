#possible supply chain issues
#TODO: research dependency vulnerabilities periodically.
import requests
import sqlite3

#Visible secret leaked
#TODO: move to env var, .gitignor-ed file, etc.
API_KEY = "VEhpcyBpcyBhIGZha2Uga2V5LCBidXQgbWF5YmUgbG9va3MgbGlrZSBvbmU="
#plaintext protocol, traffic visible to eavesdroppers, API key will be exposed in transit to API
#TODO: investigate secure protocol transmission
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
DB = None

#consider typing variables (argument(s) and return)
#TODO: apply types
def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
    }

    #missing error handling
    #TODO: surround with try/catch/except to provide graceful failure (no leakage of stack trace)
    response = requests.get(BASE_URL, params=params)

    #collect from 3rd party API
    data = response.json()
    
    #no validation of data from API
    #TODO: sanitize/validate responses from outside
    city_name = data["name"]
    temp = data["main"]["temp"]

    #insert into DB
    #variables concatenated on SQL vulnerable to injection style attacks
    #TODO: use prepared statement or stored procedure to handle DB interaction
    c = DB.cursor()
    c.execute("INSERT INTO history (city, temp) VALUES (" + city_name +", " + temp + ")")
    DB.commit()

    #str concat of outside data
    #TODO: encode variable for printing/rendering to prevent unintended eval/interpretation
    print(f"\nWeather in " + city)
    print(f"Temperature: {temp}°C")
    
if __name__ == "__main__":
    #possible access controls
    #TODO: ensure application-only rw- permissions for Database
    DB = sqlite3.connect("weather.db")
    
    #collect from user
    city = input("Enter city name: ")
    #missing error handling/input validation from user
    #TODO: apply validation, typing, and try/catch to user input before calling
    get_weather(city)
