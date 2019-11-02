import requests
import settings
import json

url = "https://www.food2fork.com/api/search"

searchQuery = "chicken"

params = {
    "key": settings.FOOD_FOR_FORK,
    "q": searchQuery
}

response = requests.request("GET", url, params=params)

with open('response.json', 'w') as outfile:
    outfile.write(response.text)
