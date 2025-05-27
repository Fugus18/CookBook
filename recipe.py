from datetime import datetime
from ingredient import IngredientInstance, IngredientData, load_ingredient_table, save_ingredient_table

ingredient_table = load_ingredient_table()


class Recipe:
    
    meal_categories = ['Breakfast', 'Appetizer', 'Soup', 'Lunch', 'Cake', 'Dessert', 'Supper', 'Drink', 'Shake', 'Smoothie', 'Snack']

    
    def __init__(self, name, categories, diets, ingredients, instructions, 
                 total_time, servings, difficulty, 
                 cuisine, author, date_created = None):
        self.name = name
        self.categories = categories if categories else []
        self.diets = diets if diets else []
        self.ingredients = ingredients if ingredients else []
        self.instructions = instructions # e.g., ["Step 1", "Step 2"]
        self.total_time = total_time
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
        print(f"Categories: {', '.join(self.categories)}")
        print(f"Diet: {', '.join(self.diets)}")
        print(f"Prep time: {self.total_time}")
        print(f"Servings: {self.servings}")
        print(f"Author: {self.author}")
        print(f"Date Created: {self.date_created}")
        print(f"Difficulty: {self.difficulty}")
        print(f"Cuisine: {self.cuisine if self.cuisine != 'None' else 'Not specified'}")
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

    def to_dict(self):
        return {
            "name": self.name,
            "categories": self.categories,
            "diets": self.diets,
            "ingredients": [ingredient.to_dict() for ingredient in self.ingredients],
            "instructions": self.instructions,
            "total_time": self.total_time,
            "servings": self.servings,
            "difficulty": self.difficulty,
            "cuisine": self.cuisine,
            "author": self.author,
            "date_created": self.date_created
        }
    
    
    @classmethod
    def from_dict(cls, data):
        ingredients = [IngredientInstance.from_dict(i) for i in data["ingredients"]]
        return cls(
            data["name"],
            data["categories"],
            data["diets"],
            ingredients,
            data["instructions"],
            int(data["total_time"]),
            data["servings"],
            data["difficulty"],
            data["cuisine"],
            data["author"],
            data.get("date_created")
        )
    
    @classmethod
    def from_input(cls):
        print('-'*30)
        name = input('Recipe name: ')
        print('-'*30)
        print('Available meal categories (you can pick multiple): ')
        print(", ".join(cls.meal_categories))
        categories = []
        print("\nEnter meal tags one by one (or press Enter to finish).")
        while True:
            category = input("Meal category: ").strip().title()
            if category.lower() == '':
                break
            if category in cls.meal_categories:
                if category not in categories:
                    categories.append(category)
                else:
                    print('Category already added')
            else:
                print('Invalid category. Try again')
        
        diets_options = ['Vegan', 'Vegetarian', 'Gluten-Free', 
                         'Dairy-Free', 'Nut-Free', 'Low-Carb', 'High-Protein']
        print('-'*30)
        print('Available diet restrictions (you can pick multiple): ')
        print(", ".join(diets_options))
        diets = []
        print("\nEnter diet restrictions one by one (or press Enter to finish).")
        while True:
            diet = input("Diet restriction: ").strip().title()
            if diet.lower() == '':
                break
            if diet in diets_options:
                if diet not in diets:
                    diets.append(diet)
                else:
                    print('Diet restriction already added')
            else:
                print('Invalid diet restriction. Try again')
        print('-'*30)
        
        ingredients = []
        print("Enter ingredients one by one (or press Enter to finish).\n")
        while True:
            ingredient = input("Ingredient name: ").strip().lower()
            if ingredient == '':
                break
            if ingredient not in ingredient_table:
                print(f"'{ingredient}' is not in the ingredient table.")
                add_new = input("Would you like to add it? (y/n): ").strip().lower()
                if add_new == 'y':
                    unit = input("Unit (e.g., g, ml, item): ").strip()
                    try:
                        base_amount = float(input("Nutritional info for (e.g., 10 for 10g/ml): "))
                        carbs = float(input("Carbohydrates per base amount: "))
                        protein = float(input("Protein per base amount: "))
                        fat = float(input("Fat per base amount: "))
                        print('\n')
                    except ValueError:
                        print("Invalid input. Skipping this ingredient.")
                        continue
            
                    # Create and add to table
                    new_data = IngredientData(unit, carbs, protein, fat, base_amount)
                    ingredient_table[ingredient] = new_data
                    # Optional: Save it to the JSON file
                    save_ingredient_table(ingredient_table)
                else:
                    continue
            try:
                amount = float(input(f"Amount in {ingredient_table[ingredient].unit}: "))
                print('\n')
                ing_obj = IngredientInstance(ingredient, amount, ingredient_table[ingredient])
                ingredients.append(ing_obj)
            except ValueError:
                print("Invalid amount. Try again.")
        print('-'*30)
    
        instructions = []
        print("Enter instruction steps one by one (or press Enter to finish).\n")
        while True:
            step = input("Step: ")
            if step.lower() == '':
                break
            instructions.append(step)
        print('-'*30)
    
        while True:
            try:
                total_time = int(input("Prep and cook time (in minutes): "))
                break
            except ValueError:
                print("Please enter a valid number.")
        
        
        servings = input("Number of servings: ")
        
        print('-'*30)
        difficulties = ['Easy', 'Medium', 'Hard']
        print('Available difficulties: ', ', '.join(difficulties))
        while True:
            difficulty = input("Difficulty: ").capitalize()
            if difficulty in difficulties:
                break
            else:
                print('Invalid difficulty. Try again')
        
        print('-'*30)        
        cuisines = ['Italian', 'Japanese', 'Mexican', 'Polish', 'Indian', 'French', 'American', 'Thai']
        print("Available cuisines (or press Enter to skip):", ", ".join(cuisines))
        while True:
            cuisine_input = input("\nSelect cuisine (or press Enter to skip): ").strip().capitalize()
            if cuisine_input == "":
                cuisine = "None"
                break
            elif cuisine_input in cuisines:
                cuisine = cuisine_input
                break
            else:
                print("Invalid cuisine. Try again.")
            
        author = input("\nAuthor name: ")
    
        return cls(name, categories, diets, ingredients, instructions,
                   total_time, servings, difficulty,
                   cuisine, author)