# EG 2nd Password Strength

# Step 1: Ask user for their password and start safety or strength score at 0, and set all requiremets to false
password = input("Enter your password")
score = 0

length_requirement = False
uppercase_requirement = False 
lowercase_requirement = False
number_requirement = False 
special_requirement = False

# Step 2: Check for the factors 
while True:
    # Length- 8 characters at least 
    if len(password) >= 8:
        length_requirement = True 
        score += 1 
        continue 
    # At least one uppercase letter 
    check_upper = any(char.isupper() for char in password)
    print(check_upper)
    # At least  one lowercase letter 
    # At least one number 
    # At least one special chararcter  

# Step 3: Calculate the safety of the password
# Length requirement +1 point 
# Containing uppercase +1 point
# Containing lowercase +1 point
# Containing a number +1 point
# Containing a special character +1 point 

# Step 4: Give a strength score
# Add the points up and print with corresponding level of strength
# Tell the user what their missing in their password
