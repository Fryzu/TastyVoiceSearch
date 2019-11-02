import requests
import settings
import json


def getReponseForIngredients(ingredients):
    url = "https://www.food2fork.com/api/search"

    searchQuery = ",".join(ingredients)

    print("Sending request for query:", searchQuery)

    params = {
        "key": settings.FOOD_FOR_FORK,
        "q": searchQuery
    }

    response = requests.request("GET", url, params=params)

    print("Response finished with code", response.status_code)

    with open('response.json', 'w') as outfile:
        outfile.write(response.text)


if __name__ == '__main__':
    getReponseForIngredients(["chicken"])
