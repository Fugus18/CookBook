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
        
    def exit_program():
        print('-'*30)
        print("Goodbye!")
        print('-'*30)

    actions = {
    "1": add_recipe,
    "2": view_recipes,
    "3": find_recipe,
    "4": remove_recipe,
    "5": exit_program,
        }

    while True:
        print("\n=== Recipe Manager ===")
        print("1. Add a recipe")
        print("2. View all recipes")
        print("3. Find a recipe")
        print("4. Remove a recipe")
        print("5. Exit\n")
    
        choice = input("Choose an option: ").strip()
        action = actions.get(choice)
        if action:
            if choice == "5":
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