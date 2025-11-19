# EG 2nd Mapping

numbers = [641,94,5619,135,4,6501,68,7,123,54,6,4]
"""divided = []

for num in numbers:
    divided.append(num/2)"""

def divide(number):
    return number/2

divided = list(map(lambda num: num/2, numbers)) 

for i, num in enumerate(numbers):
    print(f"{num} divided by 2 is {divided[i]}")