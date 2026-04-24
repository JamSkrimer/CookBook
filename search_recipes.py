def search_by_ingredient(recipes, ingredient):
    result = {}
    search_term = ingredient.lower()
    for name, data in recipes.items():
        if any(search_term in ing.lower() for ing in data["ingredients"]):
            result[name] = data
    return result