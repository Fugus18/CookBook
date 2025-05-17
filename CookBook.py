from recipe import Recipe
  
class CookBook:
    def __init__(self):
        self.recipes = []
    
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