def view_all_recipes(recipes):
    if not recipes:
        print("Книга рецептов пуста.")
        return
    for name, data in recipes.items():
        print(f"\n{name}:")
        print("  Ингредиенты:", ", ".join(data["ingredients"]))
        print("  Инструкция:", data["instructions"])