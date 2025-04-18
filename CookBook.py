from datetime import datetime

class Recipe:
    def __init__(self, name, category, ingredients, instructions, 
                 prep_time, cook_time, servings, difficulty, 
                 cuisine, author, date_created = None):
        self.name = name
        self.category = category
        self.ingredients = ingredients # e.g., {"flour": "2 cups"}
        self.instructions = instructions # e.g., ["Step 1", "Step 2"]
        self.prep_time = prep_time
        self.cook_time = cook_time
        self.servings = servings
        self.difficulty = difficulty
        self.cuisine = cuisine
        self.author = author
        self.date_created = date_created or datetime.now().strftime("%Y-%m-%d")

    def display(self):
        print('='*20)
        print(self.name.upper())
        print('='*20)
        print('Type: ',self.category)
        print(f"Category: {self.category}")
        print(f"Prep time: {self.prep_time}")
        print(f"Cook time: {self.cook_time}")
        print(f"Servings: {self.servings}")
        print(f"Author: {self.author}")
        print(f"Date Created: {self.date_created}")
        print(f"Difficulty: {self.difficulty}")
        print(f"Cuisine: {self.cuisine}")
        print('-'*20)
        print('Ingredients: ')
        for item in self.get_ingredient_list():
            print(item)
        print('\nInstructions:')
        for step in self.get_instruction_steps():
            print(step)
        print('='*20)
        
    def get_ingredient_list(self):
        return [f"- {k}: {v}" for k,v in self.ingredients.items()]

    def get_instruction_steps(self):
        return [f"{i+1}. {step}" for i, step in enumerate(self.instructions)]
    
    @classmethod
    def from_input(cls):
        name = input('Recipe name: ')
        category = input('Category name: ')
        ingredients = {}
        print("\nEnter ingredients one by one. Type 'done' when finished")
        while True:
            ingredient = input("Ingredient name (or 'done'): ")
            if ingredient.lower() == 'done':
                break
            amount = input(f'Amount for {ingredient}: ')
            ingredients[ingredient] = amount
        instructions = []
        print("\nEnter instruction steps one by one. Type 'done' when finished.")
        while True:
            step = input("Step (or 'done'): ")
            if step.lower() == 'done':
                break
            instructions.append(step)
        prep_time = input("Prep time: ")
        cook_time = input("Cook time: ")
        servings = input("Number of servings: ")
        difficulty = input("Difficulty (Easy/Medium/Hard): ")
        cuisine = input("Cuisine (e.g. 'Italian', 'Japanese'): ")
        author = input("Author name: ")
        return cls(name, category, ingredients, instructions, 
                   prep_time, cook_time, servings, difficulty,
                   cuisine, author)
    
class CookBook:
    def __init__(self):
        self.recipes = []
    
    def add_recipe(self, recipe):
        if isinstance(recipe, Recipe):
            self.recipes.append(recipe)
            print(f"'{recipe.name}' added to the cookbook")
        else:
            print('This recipe does not belong to Recipe class')

    def remove_recipe(self, recipe):
        if isinstance(recipe, Recipe):
            try:
                self.recipes.remove(recipe)
                print(f"Recipe '{recipe.name}' removed")
            except ValueError:
                print(f"Recipe '{recipe.name}' not found in the cookbook")
        else:
            print('This recipe does not belong to Recipe class')

    def list_recipes(self):
        if not self.recipes:
            print("The cookbook is empty.")
        else:
            print("Recipes in the cookbook:")
            for recipe in self.recipes:
                print(f"- {recipe.name}")
                
    def find_recipe(self, name):
        for recipe in self.recipes:
            if recipe.name.lower() == name.lower():
                recipe.display()
                return
        print(f"No recipe found with the name '{name}'.")


if __name__ == "__main__":
    cb = CookBook()
    r1 = Recipe.from_input()
    cb.add_recipe(r1)
    cb.list_recipes()
    cb.find_recipe(r1.name)
    cb.remove_recipe(r1)
    cb.list_recipes()