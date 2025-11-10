#EG 2nd Dictionaries notes
avatar = {
    "earth": {
        "Toph": "My name is Toph, cuz it sounds like TOUGH and thats just what I am"
    },
    "water": {
        "Katara": "Its not like I am a preachy crybaby who can't help but make speaches about hope all the time.",
        "Sokka": "I used to be a boomerang guy."
    },
    "fire": {
        "Zuko": "It just keeps blowing up in my face. Like everything always does!",
        "Uncle Iroh": "It's nothing but bioled leaf juice!"
    },
    "air":{
        "Aang": "Will you go penguin sledding with me!?!?"
    }
}
print(avatar["earth"]["Toph"])
print(avatar["water"]["Sokka"])

person = {
    #key: value,
    "name": "Katie",
    "age": 37,
    "job": "coordinator",
    "siblings": ["Alex", "Andrew", "Vienna", "Tia", "Treyson", "Xavier", "Jake"]
}

print(person["name"])
print(person.keys())
for key in person.keys():
    if key == "siblings":
        for sib in person[key]:
            print(f"{person['name']} has a sibling named {sib}")
    else:
        print(f"{key} is {person[key]}")
print(person.values())
person["age"] +=1
print(person["age"])
person["birthday"] = "June 8"
print(person.items())
person["birthday"] = "October 27"