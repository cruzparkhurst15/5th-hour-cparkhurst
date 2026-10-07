#Name: Cruz Parkhurst
#Class: 5th Hour
#Assignment: HW10
import random as r

#1. Print "Hello World!"
print("hello world")
#2. Create 3 variables that each randomly generate a number between 1 and 10, named A, B, and C.
a=r.randint(1,10)
b=r.randint(1,10)
c=r.randint(1,10)
#3. Print A, B, and C on the same line.
print(a,b,c)
#4. Make an if statement that prints if variable A is greater than, less than, or equal to 5.
if a>5:
    print("a is greater than 5")
elif a<5:
    print("a is less than 5")
elif a==5:
    print("a is equal to 5")
#5. Make an if statement that prints if variable B is between 3 and 7, or not.
if b>7 or b<3:
    print("b is not greater than or less than to 3 and greater than or less than to 7")
else :
    print("b is equal to 7 and 3")
#6. Make an if statement that prints if variable C is even or odd.
if c % 2 == 0:
    print("is even")
else:
    print("is odd")
#7. Create a variable whose value is 3 + a randomly generated number between 1 and 20
d=3+r.randint(1,20)
print(d)
#8. Make an if statement that prints if the variable from #7 is greater than, less than, or equal to A + B + C.
if d>a+b+c:
    print("d is greater than A,B,c")
elif d<a+b+c:
    print("d is less than A,B,c")
else:
    print("d is equal to A,B,c")