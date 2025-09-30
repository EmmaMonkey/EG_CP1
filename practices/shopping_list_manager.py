# EG 2nd Shopping List Manager 





shopping_list = []

def add_item(item):
    shopping_list.append(item)
    print(f'"{item}" was added to your shopping list.')

def remove_item(item):
    if item in shopping_list:
        shopping_list.remove(item)
        print(f'"{item}" was removed from your shopping list.')
    else:
        print(f'"{item}" is not in the list.')
    
def print_list():
    print("\nYour Shopping List:")
    if len(shopping_list) == 0:
        print("Your list is empty.")
    else:
        for i, item in enumerate(shopping_list, 1):
            print(f"{i}. {item}")

while True:
    action = input("\nWhat would you like to do? (add / remove / view / exit): ").lower()
    

    if action == "add":
        item = input("Enter the item you want to add: ")
        add_item(item)
        print_list()

    elif action == "remove":
        item = input("Enter the item you want to remove: ")
        remove_item(item)
        print_list()

    elif action == "view":
        print_list()

    elif action == "exit":
        print("Thanks for using the Shopping List Manager! Goodbye.")
        break

    else:
        print("Please type one of these: add, remove, view, or exit.")