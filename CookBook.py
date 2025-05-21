from recipe import Recipe
import json
import random
  
class CookBook:
    def __init__(self):
        self.recipes = []
        self.favorites = []
    
    def add_recipe(self, recipe):
        if isinstance(recipe, Recipe):
            self.recipes.append(recipe)
            print('-'*30)
            print(f"'{recipe.name}' added to the cookbook")
            print('-'*30)
        else:
            print('This recipe does not belong to Recipe class')

    def list_recipes(self):
        if not self.recipes:
            print('-'*30)
            print("The cookbook is empty.")
            print('-'*30)
        else:
            print('-'*30)
            print("Recipes in the cookbook:")
            for recipe in self.recipes:
                print(f"- {recipe.name}")
            print('-'*30)
                
    def find_recipe(self, name):
        for recipe in self.recipes:
            if recipe.name.lower() == name.lower():
                print('\n')
                recipe.display()
                return
        print('-'*30)
        print(f"No recipe found with the name '{name}'.")
        print('-'*30)
        
    def remove_recipe(self, name):
        to_remove = next((r for r in self.recipes if r.name.lower() == name.lower()), None)
        if to_remove:
            self.recipes.remove(to_remove)
            print('-'*30)
            print(f"Recipe '{to_remove.name}' removed")
            print('-'*30)
        else:
            print('-'*30)
            print(f"Recipe '{name}' not found in the cookbook")
            print('-'*30)
            
    def save_to_file(self, filename):
        data = {
        "recipes": [r.to_dict() for r in self.recipes],
        "favorites": [r.name for r in self.favorites]  # Save by name
    }
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        print(f"Cookbook saved to '{filename}'")

    def load_from_file(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
            self.recipes = [Recipe.from_dict(r) for r in data.get("recipes", [])]
    
            # Restore favorites by matching names
            favorite_names = data.get("favorites", [])
            self.favorites = [
                r for r in self.recipes if r.name in favorite_names
            ]
            print(f"Cookbook loaded from '{filename}'")
        except FileNotFoundError:
            print(f"No such file: '{filename}'")
        except json.JSONDecodeError:
            print(f"Invalid JSON format in file: '{filename}'")
            
    def mark_favorite(self, name):
        to_mark = next((m for m in self.recipes if m.name.lower() == name.lower()), None)
        if to_mark:
            if to_mark not in self.favorites:
                self.favorites.append(to_mark)
                print('-'*30)
                print(f"Recipe '{to_mark.name}' marked as favorite")
                print('-'*30)
            else:
                print('-'*30)
                print(f"Recipe '{name}' is already in favorites")
                print('-'*30)
        else:
            print('-'*30)
            print(f"Recipe '{name}' not found in the cookbook")
            print('-'*30)
    
    def view_favorites(self):
        if not self.favorites:
            print('-'*30)
            print("No favorite recipes yet.")
            print('-'*30)
        else:
            print('-'*30)
            print("Favorite Recipes:")
            for recipe in self.favorites:
                print(f"- {recipe.name}")
            print('-'*30)
            
    def unmark_favorite(self, name):
        recipe = next((r for r in self.favorites if r.name.lower() == name.lower()), None)
        if recipe:
            self.favorites.remove(recipe)
            print('-'*30)
            print(f"Recipe '{recipe.name}' removed from favorites")
            print('-'*30)
        else:
            print('-'*30)
            print(f"Recipe '{name}' is not in favorites")
            print('-'*30)
            
    def draw_random_meal(self):
        print('-' * 30)
        print("Available Meal Categories:")
        print(", ".join(Recipe.meal_categories))
        print('-' * 30)
        category = input("Enter the category to draw from: ").strip().lower()
    
        filtered = [
            r for r in self.recipes
            if any(c.lower() == category for c in r.categories)
        ]
    
        if not filtered:
            print('-' * 30)
            print(f"No meals found in category '{category.capitalize()}'.")
            print('-' * 30)
            return
    
        selected = random.choice(filtered)
        print('-' * 30)
        print(f"🎲 You got: {selected.name}")
        print('-' * 30)
    
        show = input("Do you want to see the full recipe? (y/n): ").strip().lower()
        if show == 'y':
            selected.display()