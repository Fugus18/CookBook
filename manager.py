from cookbook import CookBook
from recipe import Recipe

def main():
    cookbook_obj = CookBook()

    def add_recipe():
        recipe = Recipe.from_input()
        cookbook_obj.add_recipe(recipe)

    def view_recipes():
        cookbook_obj.list_recipes()
    
    def find_recipe():
        name = input("Enter the recipe name to find: ").strip()
        cookbook_obj.find_recipe(name)
    
    def remove_recipe():
        name = input("Enter the recipe name to remove: ").strip()
        cookbook_obj.remove_recipe(name)
        
    def save_cookbook():
        filename = input("Enter filename to save: ").strip()+'.json'
        cookbook_obj.save_to_file(filename)

    def load_cookbook():
        filename = input("Enter filename to load: ").strip()+'.json'
        cookbook_obj.load_from_file(filename)
        
    def mark_favorite():
        name = input("Enter the recipe name to mark as favorite: ").strip()
        cookbook_obj.mark_favorite(name)
    
    def view_favorites():
        cookbook_obj.view_favorites()
    
    def unmark_favorite():
        name = input("Enter the recipe name to unmark as favorite: ").strip()
        cookbook_obj.unmark_favorite(name)
    
    def draw_random_meal():
        cookbook_obj.draw_random_meal()
        
    def generate_grocery_list():
        cookbook_obj.generate_grocery_list()

    def filter_recipes():
        print("\nEnter filter criteria. Press Enter to skip a criterion.\n")
        category = input("Filter by category: ").strip()
        ingredient = input("Filter by ingredient: ").strip()
        try:
            total_time = input("Max total time in minutes: ").strip()
            total_time = int(total_time) if total_time else None
        except ValueError:
            total_time = None
        difficulty = input("Filter by difficulty: ").strip()
        cuisine = input("Filter by cuisine: ").strip()
        author = input("Filter by author: ").strip()
    
        criteria = {}
        if category: criteria["category"] = category
        if ingredient: criteria["ingredient"] = ingredient
        if total_time is not None: criteria["total_time"] = total_time
        if difficulty: criteria["difficulty"] = difficulty
        if cuisine: criteria["cuisine"] = cuisine
        if author: criteria["author"] = author
    
        cookbook_obj.filter_recipes(criteria)
        

    def exit_program():
        print('-'*30)
        print("Goodbye!")
        print('-'*30)

    actions = {
    "1": add_recipe,
    "2": view_recipes,
    "3": find_recipe,
    "4": remove_recipe,
    "5": save_cookbook,
    "6": load_cookbook,
    "7": mark_favorite,
    "8": view_favorites,
    "9": unmark_favorite,
    "10": draw_random_meal,
    "11": generate_grocery_list,
    "12": filter_recipes,
    "13": exit_program,
}

    while True:
        print("\n=== Recipe Manager ===")
        print("Recipe")
        print(" 1. Add a recipe")
        print(" 2. View all recipes")
        print(" 3. Find a recipe")
        print(" 4. Remove a recipe")
        print("Cookbook")
        print(" 5. Save cookbook to file")
        print(" 6. Load cookbook from file")
        print("Favorites")
        print(" 7. Mark recipe as favorite")
        print(" 8. View favorite recipes")
        print(" 9. Remove recipe from favorites")
        print("Other")
        print(" 10. Draw a random recipe from a category")
        print(" 11. Generate grocery list")
        print(" 12. Filter for specified variable")


        print("13. Exit\n")
    
        choice = input("Choose an option: ").strip()
        action = actions.get(choice)
        if action:
            if choice == "13":
                action()
                break
            else:
                action()
        else:
            print('-'*30)
            print("Invalid option. Please choose 1-5.")
            print('-'*30)

if __name__ == "__main__":
    main()