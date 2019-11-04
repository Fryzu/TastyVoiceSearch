import requests
import settings


def getReponseForIngredients(ingredients):
    '''Gets response from food2fork for ingredients list 
    and returns and saves the result in response.json'''

    url = "https://www.food2fork.com/api/search"

    searchQuery = ",".join(ingredients)

    print("Sending request for query:", searchQuery)

    params = {
        "key": settings.FOOD_FOR_FORK,
        "q": searchQuery
    }

    response = requests.request("GET", url, params=params)

    print("Response finished with code", response.status_code)

    with open('output/response.json', 'w') as outfile:
        outfile.write(response.text)

    return response.text


if __name__ == '__main__':
    getReponseForIngredients(["chicken"])
