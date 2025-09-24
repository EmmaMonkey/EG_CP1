# EG 2nd What is my grade

grade = float(input("What is your grade percentage without the percentage sign: "))

if grade >= 94:
    print("You have an A")
elif grade >= 90:
    print("You have an A-")
elif grade >= 87:
    print("You have a B+")
elif grade >= 84:
    print("You have a B")
elif grade >= 80:
    print("You have a B-")
elif grade >= 77:
    print("You have a C+")
elif grade >= 74:
    print("You have a C")
elif grade >= 70:
    print("You have a C-")
elif grade >= 67:
    print("You have a D+")
elif grade >= 64:
    print("You have a D")
elif grade >= 60:
    print("You have a D-")
else:
    print("You have an F")