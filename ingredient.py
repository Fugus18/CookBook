import json
from pathlib import Path

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
    
    def to_dict(self):
        return {
            "unit": self.unit,
            "carbs": self.carbs,
            "protein": self.protein,
            "fat": self.fat,
            "base_amount": self.base_amount
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            unit=data["unit"],
            carbs=data["carbs"],
            protein=data["protein"],
            fat=data["fat"],
            base_amount=data["base_amount"]
        )
    
class IngredientInstance:
    def __init__(self, name, amount, ingredient_data):
        self.name = name
        self.amount = amount
        self.ingredient_data = ingredient_data

    def get_nutrition(self):
        return self.ingredient_data.calculate_nutrition(self.amount)

    def to_dict(self):
        return {
            "name": self.name,
            "amount": self.amount,
            "ingredient_data": self.ingredient_data.to_dict()
        }

    @classmethod
    def from_dict(cls, data):
        from ingredient import IngredientData
        ingredient_data = IngredientData.from_dict(data["ingredient_data"])
        return cls(
            name=data["name"],
            amount=data["amount"],
            ingredient_data=ingredient_data
        )

def load_ingredient_table(filepath="ingredient_data.json"):
    path = Path(filepath)
    if not path.exists():
        raise FileNotFoundError(f"Ingredient data file '{filepath}' not found.")
    
    with open(filepath, "r", encoding="utf-8") as f:
        raw_data = json.load(f)
        return {
            name.lower(): IngredientData(**data)
            for name, data in raw_data.items()
        }
    
def save_ingredient_table(table, filepath="ingredient_data.json"):
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump({name: data.to_dict() for name, data in table.items()}, f, indent=2)



# If you want some testing/demo code for this file, use the usual guard:
if __name__ == "__main__":
    # Example usage:
    print('Witam')