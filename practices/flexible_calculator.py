#EG 2nd Flexible Calculator 

#define the calculator function
# make the list
# display the options
# make the action happen
def calculator(*numbers, **info):
    operation = info.get("operation", "sum")  # default is sum
   
    if operation == "sum":
        return sum(numbers)
    elif operation == "average":
        return sum(numbers) / len(numbers)  # calculate average manually
    elif operation == "max":
        return max(numbers)
    elif operation == "min":
        return min(numbers)
    elif operation == "product":
        product = 1
        for num in numbers:
            product *= num
        return product
    else:
        return "Invalid operation."

# welcome the user
print("Welcome to the Flexible Calculator!\n")

# main code
while True:
    # display the options
    print("Available operations: sum, average, max, min, product")
    operation = input("Which operation would you like to perform? ").lower()
   
    # make the list of numbers
    numbers = []
    print("Enter numbers (type 'done' when finished):")
   
    while True:
        value = input("Number: ")
        if value.lower() == "done":
            break
        # check if input is a number (integer or float)
        if value.replace(".", "", 1).isdigit():
            numbers.append(float(value))
        else:
            print("Please enter a valid number.")
   
    if len(numbers) == 0:
        print("No numbers entered. Try again.\n")
        continue
   
    # make the action happen
    print(f"\nCalculating {operation} of: {', '.join(map(str, numbers))}")
    result = calculator(*numbers, operation=operation)
    print(f"Result: {result}\n")
   
    # exit the program
    again = input("Would you like to perform another calculation? (yes/no) ").lower()
    if again != "yes":
        print("\nThank you for using the Flexible Calculator!")
        break