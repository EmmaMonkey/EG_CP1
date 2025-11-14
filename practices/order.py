
# Menu dictionary
menu = {
    "Main Dishes": {
        "The Box Combo": 11.99,
        "The 3 Finger Combo": 10.39,
        "The Caniac Combo": 17.29,
        "The Sandwich Combo": 10.79,
        "The Kids Combo": 6.99,
    },
    "Side Dishes": {
        "Chicken Fingers": 1.99,
        "Crinkle-Cut Fries": 2.59,
        "Cane's Sauce": 0.39,
        "Texas Toast": 1.35,
        "Coleslaw": 1.35,
        "Sandwich": 8.49,
    },
    "Drink": {
        "Lemonade": 2.79,
        "Sweet Tea": 2.49,
        "Coke": 2.49,
        "Diet Coke": 2.49,
        "Coke Zero": 2.49,
        "Sprite": 2.49,
        "Fanta": 2.49,
    }
}

print("Welcome to Order Up!")

# Show menu
print("\nMain Dishes:", menu["Main Dishes"])
print("Side Dishes:", menu["Side Dishes"])
print("Drinks:", menu["Drink"])

# Ask for items
main = input("\nEnter your main dish: ")
drink = input("Enter your drink: ")
side1 = input("Enter your first side dish: ")
side2 = input("Enter your second side dish: ")

# Calculate total
total = menu["Main Dishes"][main] + menu["Drink"][drink] + menu["Side Dishes"][side1] + menu["Side Dishes"][side2]

# Print order summary
print("\nYour Order:")
print("Main Dish:", main)
print("Drink:", drink)
print("Side Dish 1:", side1)
print("Side Dish 2:", side2)
print("Total Cost: $", round(total, 2))