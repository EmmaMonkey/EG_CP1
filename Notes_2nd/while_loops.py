# EG 2nd While Loops Notes
import time
import random

#Infinite Loop
num = 1
break_point = random.randint(1,30)
while num < 20:
    num += 1  #fixed the loop
    if num == break_point:
        break
    elif num%2 != 0:
        continue
    print(num)
    time.sleep(.10)
else:  
    print("This loop exited by meeting the condition!")

print("The loop is over")



#for num in range (1,21):
  #  print(num)
#while num <=20:
    #print(num)
    #numt=1

