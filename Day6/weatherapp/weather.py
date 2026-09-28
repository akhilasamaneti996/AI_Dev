import requests
API_KEY = "457ad1867530a50b50f2bd12d0c0653b"
city=input("Enter city name: ")
url="https://home.openweathermap.org/api_keys"
parameters={
    "q":city,
    "appid": API_KEY,
    "units":"metric"
}
response=requests.get(url.param)