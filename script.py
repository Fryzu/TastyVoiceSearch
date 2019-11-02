import requests

url = "https://tasty.p.rapidapi.com/recipes/auto-complete"

querystring = {"prefix": "apple"}

headers = {
    'x-rapidapi-host': "tasty.p.rapidapi.com",
    'x-rapidapi-key': "SIGN-UP-FOR-KEY"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
