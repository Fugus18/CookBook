# 🥘 CookBook

A simple and extendable Python CLI app for managing recipes and tracking nutrition.

## 💡 Features

- Add, view, and remove recipes
- Store ingredients with nutrition data
- Auto-calculate calories, protein, carbs, and fat
- Mark recipes as favorites
- Filter and search recipes by various criteria
- Draw a random meal from a category
- Generate a grocery list
- Save/load recipes from JSON files
- Support for custom ingredients

## 🚀 Getting Started

1. Clone the repo:
   ```bash
   git clone https://github.com/JakubFlak/CookBook.git
   cd CookBook
   ```
2. Run the app:
   ```
   python manager.py
   ```
3. Follow the prompts to input and manage recipes.

## 📂 Structure
- manager.py – CLI interface
- cookbook.py – CookBook logic
- recipe.py – Recipe object
- ingredient.py – Ingredient data and nutrition logic
- ingredient_data.json – Nutrition info for known ingredients
- witam.json – Sample saved cookbook