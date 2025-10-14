# EG 2nd Password Strength

# Step 1: Ask user for their password and start safety or strength score at 0, and set all requiremets to false
password = input("Enter your password")
score = 0

length_requirement = False
uppercase_requirement = False 
lowercase_requirement = False
number_requirement = False 
special_requirement = False

#Define Special Characters
special_characters = ["!","@","#","$","%","^","&","*","(",")","-","_","=","+",".",",","\"",":",";","<",">","?","[","]","}","{","|"]

# Step 2: Check for the factors, if any requirements meet set the boolean to true
    # Length- 8 characters at least 
if len(password) >= 8:
    length_requirement = True
    score += 1 
# At least one uppercase letter 
if any(char.isupper() for char in password):
    uppercase_requirement = True
    score +=1
        
 # At least  one lowercase letter 
if any(char.islower() for char in password):
    lowercase_requirement = True 
    score += 1 

# At least one number 
   
if any(char.isdigit() for char in password):
    number_requirement = True 
    score += 1 
        
# At least one special chararcter  
for item in special_characters:
    if item in password:
        special_requirement = True
        score += 1 
        break



# Step 3: Calculate the safety of the password
# Length requirement +1 point 
# Containing uppercase +1 point
# Containing lowercase +1 point
# Containing a number +1 point
# Containing a special character +1 point 

# Display Password Strength Assesment
print(f"Password Strength Assessment:\nLength (8+ Characters): {length_requirement}\nContains Uppercase:{uppercase_requirement}\nContains Lowercase: {lowercase_requirement}\nContains a Number: {number_requirement}\nContains a Special Character: {special_requirement}\n")

# Step 4: Give a strength score
# Add the points up and print with corresponding level of strength
if score == 1 or score == 2:
    print(f"Strength Score: {score}/5\nPassword Strength: Weak")
elif score == 3:
    print(f"Strength Score: {score}/5\nPassword Strength: Moderate")
elif score == 4:
    print(f"Strength Score: {score}/5\nPassword Strength: Strong")
elif score == 5: 
    print(f"Strength Score: {score}/5\nPassword Strength: Very Strong")
else:
    print("This shouldn't be possible")
# Tell the user what their missing in their password

