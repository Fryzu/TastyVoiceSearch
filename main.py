from utils.fork import getReponseForIngredients
from utils.ingredients import get_ingredients

if __name__ == '__main__':
    ingredients = get_ingredients()
    getReponseForIngredients(ingredients)
