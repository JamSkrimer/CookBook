def delete_recipe(recipes, name):
    if name in recipes:
        del recipes[name]
        print(f"Рецепт '{name}' удалён.")
        return True
    print(f"Рецепт '{name}' не найден.")
    return False