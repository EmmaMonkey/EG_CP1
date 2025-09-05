# EG 2nd String Method Notes

name = input("What is your name").strip().lower().capitalize().title()
#.lower() => makes it all lower case 
#.upper() => all upper case
#.capitalize() => capitalizes the first letter
#.title() => capitalizes the first letter of every word

age = int(input("Gurt how old are you"))
#print("Hello {}, It is nice to meet you! I cant believe you are {:.2f}!".format(name, age))
print(f"Hello {name}, It is nice to meet you! I cant believe you are {age:.1f}!")
age = floatinput("Gurt how old are you") # type: ignore

#print(age.isdigit())

#print("Really?,"+age+", you is old unc")

#sentence = "The quick brown fox jumps over the lazy dog!"

#word = "brown"
#start = (sentence.find(word))
#length = len(word)

#print(sentence.replace(word,"yellow"))


#print(sentence.replace(word, "yellow"))