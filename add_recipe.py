def add_recipe(recipes, name, ingredients, instructions):
    recipes[name] = {
        "ingredients": ingredients,
        "instructions": instructions
    }
    print(f"Рецепт '{name}' добавлен.")