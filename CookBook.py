from datetime import datetime

class Recipe:
    def __init__(self, name, category, ingredients, instructions, 
                 prep_time, cook_time, servings, difficulty, 
                 cuisine, author, date_created = None):
        self.name = name
        self.category = category
        self.ingredients = ingredients if ingredients else []
        self.instructions = instructions # e.g., ["Step 1", "Step 2"]
        self.prep_time = prep_time
        self.cook_time = cook_time
        self.servings = servings
        self.difficulty = difficulty
        self.cuisine = cuisine
        self.author = author
        self.date_created = date_created or datetime.now().strftime("%Y-%m-%d")

    def display_nutrition(self):
        total = {"carbohydrates": 0, "protein": 0, "fat": 0, "calories": 0}
        for ing in self.ingredients:
            nut = ing.get_nutrition()
            for key in total:
                total[key] += nut[key]
        print("Estimated Nutrition (Total):")
        print(f"Carbohydrates: {total['carbohydrates']:.1f}g")
        print(f"Protein: {total['protein']:.1f}g")
        print(f"Fat: {total['fat']:.1f}g")
        print(f"Calories: {total['calories']:.0f} kcal")

    def display(self):
        print('=' * 30)
        print(self.name.upper())
        print('=' * 30)
        print(f"Type: {self.category}")
        print(f"Prep time: {self.prep_time}")
        print(f"Cook time: {self.cook_time}")
        print(f"Servings: {self.servings}")
        print(f"Author: {self.author}")
        print(f"Date Created: {self.date_created}")
        print(f"Difficulty: {self.difficulty}")
        print(f"Cuisine: {self.cuisine}")
        print('-' * 30)
        print("Ingredients:")
        for item in self.get_ingredient_list():
            print(item)
        print('-'*30)
        print('Instructions:')
        for step in self.get_instruction_steps():
            print(step)
        print('-' * 30)
        self.display_nutrition()
        print('=' * 30)
        
    def get_ingredient_list(self):
        result = []
        for ing in self.ingredients:
            result.append(f"- {ing.amount} {ing.ingredient_data.unit} {ing.name}")
        return result
    def get_instruction_steps(self):
        return [f"{i+1}. {step}" for i, step in enumerate(self.instructions)]

    
    
    @classmethod
    def from_input(cls):
        name = input('Recipe name: ')
        category = input('Category name: ')
        ingredients = []
    
        print("\nEnter ingredients one by one. Type 'done' when finished.")
        while True:
            ingredient = input("Ingredient name (or 'done'): ").strip().lower()
            if ingredient == 'done':
                break
            if ingredient not in ingredient_table:
                print(f"'{ingredient}' is not in the ingredient table.")
                continue
            try:
                amount = float(input(f"Amount in {ingredient_table[ingredient].unit}: "))
                ing_obj = IngredientInstance(ingredient, amount, ingredient_table[ingredient])
                ingredients.append(ing_obj)
            except ValueError:
                print("Invalid amount. Try again.")
    
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
            print('-'*30)
            print(f"'{recipe.name}' added to the cookbook")
            print('-'*30)
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
                print('\n')
                recipe.display()
                return
        print('-'*30)
        print(f"No recipe found with the name '{name}'.")
        print('-'*30)

class IngredientData:
    def __init__(self, unit, carbs, protein, fat, base_amount):
        self.unit = unit
        self.carbs = carbs
        self.protein = protein
        self.fat = fat
        self.base_amount = base_amount  # e.g., 10 (for 10g) or 1 (for 1 item)

    def calculate_nutrition(self, amount):
        factor = amount / self.base_amount
        return {
            "carbohydrates": self.carbs * factor,
            "protein": self.protein * factor,
            "fat": self.fat * factor,
            "calories": round(
                (self.carbs * factor * 4) + 
                (self.protein * factor * 4) + 
                (self.fat * factor * 9), 2
            )
        }
    
class IngredientInstance:
    def __init__(self, name, amount, ingredient_data):
        self.name = name
        self.amount = amount
        self.ingredient_data = ingredient_data

    def get_nutrition(self):
        return self.ingredient_data.calculate_nutrition(self.amount)
  
    

if __name__ == "__main__":
    # Create a sample ingredient database
    # C:P:F
    ingredient_table = {
    "egg": IngredientData("item", 0.6, 6.0, 5.0, base_amount=1),  # per 1 egg (50g)
    "flour": IngredientData("g", 7.6, 1.0, 0.1, base_amount=10),   # per 10g plain flour
    "sugar": IngredientData("g", 10.0, 0.0, 0.0, base_amount=10),  # per 10g granulated sugar
    "butter": IngredientData("g", 0.01, 0.09, 8.1, base_amount=10),  # per 10g unsalted butter
    "milk": IngredientData("ml", 0.47, 0.33, 0.39, base_amount=10),  # per 10ml whole milk
    "chicken breast": IngredientData("g", 0.0, 3.1, 0.36, base_amount=10),  # per 10g skinless chicken breast
    "carrot": IngredientData("g", 0.96, 0.09, 0.02, base_amount=10),  # per 10g raw carrot
    "tomato": IngredientData("g", 0.39, 0.09, 0.02, base_amount=10),  # per 10g raw tomato
    "rice": IngredientData("g", 2.8, 0.27, 0.03, base_amount=10),  # per 10g cooked white rice
    "potato": IngredientData("g", 1.75, 0.2, 0.01, base_amount=10),  # per 10g boiled potato
    "spinach": IngredientData("g", 0.36, 0.29, 0.04, base_amount=10),  # per 10g raw spinach
    "cheddar cheese": IngredientData("g", 0.13, 2.5, 3.3, base_amount=10),  # per 10g cheddar cheese
    "banana": IngredientData("g", 2.28, 0.13, 0.03, base_amount=10),  # per 10g banana
    "avocado": IngredientData("g", 0.85, 0.2, 1.5, base_amount=10),  # per 10g avocado
    "olive oil": IngredientData("g", 0.0, 0.0, 10.0, base_amount=10),  # per 10g olive oil
    "onion": IngredientData("g", 0.93, 0.09, 0.01, base_amount=10),  # per 10g raw onion
    "garlic": IngredientData("g", 3.31, 0.64, 0.05, base_amount=10),  # per 10g raw garlic
    "apple": IngredientData("g", 1.14, 0.05, 0.03, base_amount=10),  # per 10g apple
    "salmon": IngredientData("g", 0.0, 2.5, 1.4, base_amount=10),  # per 10g raw salmon
    "beef steak": IngredientData("g", 0.0, 2.6, 2.0, base_amount=10),  # per 10g beef steak
}


    cookbook = CookBook()

    while True:
        print("\n=== Recipe Manager ===")
        print("1. Add a recipe")
        print("2. View all recipes")
        print("3. Find a recipe")
        print("4. Remove a recipe")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            recipe = Recipe.from_input()
            cookbook.add_recipe(recipe)
        elif choice == "2":
            print('-'*30)
            cookbook.list_recipes()
            print('-'*30)
        elif choice == "3":
            name = input("Enter the recipe name to find: ")
            cookbook.find_recipe(name)
        elif choice == "4":
            name = input("Enter the recipe name to remove: ")
            # Find the actual recipe object to remove
            to_remove = next((r for r in cookbook.recipes if r.name.lower() == name.lower()), None)
            if to_remove:
                cookbook.remove_recipe(to_remove)
            else:
                print('-'*30)
                print(f"Recipe '{name}' not found.")
                print('-'*30)
        elif choice == "5":
            print('-'*30)
            print("Goodbye!")
            print('-'*30)
            break
        else:
            print("Invalid option. Please choose 1-5.")
