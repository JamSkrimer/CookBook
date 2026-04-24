import json

DATA_FILE = "recipes.json"

from add_recipe import add_recipe
from search_recipes import search_by_ingredient
from view_recipes import view_all_recipes
from delete_recipe import delete_recipe

def load_recipes():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_recipes(recipes):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(recipes, f, ensure_ascii=False, indent=4)

def main():
    recipes = load_recipes()

    while True:
        print("\n--- Книга рецептов ---")
        print("1. Добавить рецепт")
        print("2. Найти рецепты по ингредиенту")
        print("3. Показать все рецепты")
        print("4. Удалить рецепт")
        print("5. Выход")
        choice = input("Выберите действие: ")

        if choice == "1":
            name = input("Название рецепта: ")
            ingredients = input("Ингредиенты (через запятую): ").split(",")
            ingredients = [ing.strip() for ing in ingredients]
            instructions = input("Инструкция: ")
            add_recipe(recipes, name, ingredients, instructions)
            save_recipes(recipes)

        elif choice == "2":
            ingredient = input("Введите ингредиент для поиска: ")
            found = search_by_ingredient(recipes, ingredient)
            if found:
                view_all_recipes(found)
            else:
                print("Ничего не найдено.")

        elif choice == "3":
            view_all_recipes(recipes)

        elif choice == "4":
            name = input("Название удаляемого рецепта: ")
            if delete_recipe(recipes, name):
                save_recipes(recipes)

        elif choice == "5":
            print("До свидания!")
            break
        else:
            print("Неверный ввод. Попробуйте снова.")

if __name__ == "__main__":
    main()