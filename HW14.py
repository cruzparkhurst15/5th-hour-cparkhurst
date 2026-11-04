#Name:
#Class: 5th Hour
#Assignment: HW14
import random as r
import time
#1. Create a while loop with variable i that counts down from 5 to 0 and then prints
#"Hello World!" at the end.
i= 5
while i >= 0:
    print (i)
    time.sleep( 0.1)
    i -=1
else:
    print ("hello mack")
#2. Create a while loop that prints only even numbers between 1 and 30 (HINT: modulo).
j= 1
while j >= 0:
    if j % 2 == 0:
        print (j)
    time.sleep(0.1)
    j += 1
    if j ==32:
        break
#3. Create a while loop that prints from 1 to 30 and continues (skips the number) if the
#number is divisible by 3.
k= 1
while k<=30:
    if k % 3 == 0:
        k +=1
        continue
    print (k)
    k +=1
#4. Create a while loop that randomly generates a number between 1 and 6, prints the result,
#and then breaks the loop if it's a 1.
l= r.randint(1, 6)
while l != 6:
    if l ==1:
        break
    print (l)
    l= r.randint(1, 6)
#5. Create a while loop that asks for a number input until the user inputs the number 0.
Num0 = int(input("Enter the seceret number"))
while Num0 != 0:
    Num0 = int(input("Enter the seceret number"))