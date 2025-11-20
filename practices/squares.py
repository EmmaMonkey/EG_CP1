#EG 2nd Squared Numbers
# List the numbers
numbers = [641,94,5619,135,4,6501,68,7,123,54,6,4,67,42,2,23,4,35,465,354,24,1,4323,634,543,636,546,42,43235,]

# Main Code
def square(number):
    return (number ** 2)
#use map and Lambda 
squared = list(map(lambda num : (num**2), numbers)) 

for i, num in enumerate(numbers):
    print(f"{num} squared is {squared[i]}")