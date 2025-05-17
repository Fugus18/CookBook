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

# The ingredient table as a module-level variable
ingredient_table = {
    "egg": IngredientData("item", 0.6, 6.0, 5.0, base_amount=1),
    "flour": IngredientData("g", 7.6, 1.0, 0.1, base_amount=10),
    "sugar": IngredientData("g", 10.0, 0.0, 0.0, base_amount=10),
    "butter": IngredientData("g", 0.01, 0.09, 8.1, base_amount=10),
    "milk": IngredientData("ml", 0.47, 0.33, 0.39, base_amount=10),
    "chicken breast": IngredientData("g", 0.0, 3.1, 0.36, base_amount=10),
    "carrot": IngredientData("g", 0.96, 0.09, 0.02, base_amount=10),
    "tomato": IngredientData("g", 0.39, 0.09, 0.02, base_amount=10),
    "rice": IngredientData("g", 2.8, 0.27, 0.03, base_amount=10),
    "potato": IngredientData("g", 1.75, 0.2, 0.01, base_amount=10),
    "spinach": IngredientData("g", 0.36, 0.29, 0.04, base_amount=10),
    "cheddar cheese": IngredientData("g", 0.13, 2.5, 3.3, base_amount=10),
    "banana": IngredientData("g", 2.28, 0.13, 0.03, base_amount=10),
    "avocado": IngredientData("g", 0.85, 0.2, 1.5, base_amount=10),
    "olive oil": IngredientData("g", 0.0, 0.0, 10.0, base_amount=10),
    "onion": IngredientData("g", 0.93, 0.09, 0.01, base_amount=10),
    "garlic": IngredientData("g", 3.31, 0.64, 0.05, base_amount=10),
    "apple": IngredientData("g", 1.14, 0.05, 0.03, base_amount=10),
    "salmon": IngredientData("g", 0.0, 2.5, 1.4, base_amount=10),
    "beef steak": IngredientData("g", 0.0, 2.6, 2.0, base_amount=10),
}

# If you want some testing/demo code for this file, use the usual guard:
if __name__ == "__main__":
    # Example usage:
    egg = ingredient_table["egg"]
    nutrition = egg.calculate_nutrition(2)  # nutrition for 2 eggs
    print(f"Nutrition for 2 eggs: {nutrition}")