from TastyVoiceSearch.utils.fork import getReponseForIngredients
from TastyVoiceSearch.utils.ingredients import get_ingredients

if __name__ == '__main__':
    ingredients = get_ingredients()
    getReponseForIngredients(ingredients)
