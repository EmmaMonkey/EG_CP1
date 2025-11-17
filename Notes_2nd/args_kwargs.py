# EG 2nd period *args and **kwargs

"""def hello(name="Tia", age=29):
    return f"Hello {name}! You are {age}!"

print(hello())
print(hello("Xavier"))
print(hello("Treyson", 19))"""

def hello(*names, last, vlast):
    print(type(names))
    for name in names:
        if name == "Vienna":
            print(f"Hello {name} {last} {vlast}")
        else:
            print(f"Hello {name} {last}")

hello("Alex", "Katie", "Andrew", "Vienna", "Tia", "Treyson", "Xavier", "Jake", last = "LaRose", vlast = "Atkin")

def hello(*names, last, vlast):
    print(type(names))
    for name in names:
        if name == "Vienna":
            print(f"Hello {name} {last} {vlast}")
        else:
            print(f"Hello {name} {last}")

hello("Alex", "Katie", "Andrew", "Vienna", "Tia", "Treyson", "Xavier", "Jake", last = "LaRose", vlast = "Atkin")