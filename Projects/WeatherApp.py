import requests
import json
city = input("Enter the name of the city \n")

url = f"https://api.weatherapi.com/v1/current.json?key=06defd859c9f47768e0111807242005&q={city}"

r = requests.get(url)
# print(r.text)
weatherdic = json.loads(r.text)

if "current" in weatherdic and "temp_c" in weatherdic["current"]:
    print(weatherdic["current"]["temp_c"])
else:
    print("Error: Could not retrieve the temperature data.")