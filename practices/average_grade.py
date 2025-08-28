#EG 2nd Average Grade 

p1=float(input("What is your grade in first period?\n"))
p2=float(input("What is your grade in second period?\n"))
p3=float(input("What is your grade in third period?\n"))
p4=float(input("What is your grade in fourth period?\n"))
p5=float(input("What is your grade in five period?\n"))
p6=float(input("What is your grade in sixth period?\n"))
p7=float(input("What is your grade in seventh period?\n"))

avg = round((p1+p2+p3+p4+p5+p6+p7)/7, 2)

print("Your average grade is :", avg)
