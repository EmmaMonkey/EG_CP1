# EG 2nd Elif and Logical Operators Notes

homework = False
chores = True
room = True

if homework and chores and room:
    print("You can go to your friends house.")
elif not chores or not room:
    print("Do your chores!")
else:
    print("Go do your homework.")

username = input("Enter your username: ")
password = input("Enter your password: ")

if username == "MsLaRose" and password == "1234":
    print("Welcome Ms. LaRose")
elif username == "Tia" and password == "password":
    print("Welcome Tia")
elif username == "Andrew" and password == "orange":
    print("Welcome Andrew")
else:
    print("That is not a valid sign in.")
    