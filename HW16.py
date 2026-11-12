#Name:Cruz Parkhusrt
#Class: 5th Hour
#Assignment: HW16


#1. import the "random" library
import random as r
import math
#2. print "Hello World!"
print('hello world')
#3. Create three variables named a, b, and c, and allow the user to input an integer for each.
a =int(input('enter a number'))
b=int(input('enter a number'))
c=int(input('enter a number'))

#4. Add a and b together, then divide the sum by c. Print the result.
mack = (a+b) /c
print(mack)
#5. Round the result from #3 up or down, and then determine if it is even or odd.
d=(round(mack))
if d % 2 == 0:
    print('even')
else:
    print('odd')
#6. Create a list of five different random integers between 1 and 10.
jake= [r.randint(1,10),r.randint(1,10),r.randint(1,10),r.randint(1,10),r.randint(1,10)]
print(jake)
#7. Print the 4th number in the list.
print(jake[3])

#8. Append another integer to the end of the list, also random from 1 to 10.
jake.append(r.randint(1,10))
print(jake)
#9. Sort the list from lowest to highest and then print the 4th number in the list again.
jake.sort ()
print(jake)

#10. Create a while loop that starts at 1, prints i and then adds i to itself until it is greater than 100.
i=1
while i<100:
    print(i)
    i+=i
#11. Create a list containing the names of five other students in the classroom.
name = ('lilla','jakie','niily','ethin','aaaatony')

#12. Create a for loop that individually prints out the names of each student in the list.
for g in name:
    print(g)
#13. Create a for loop that counts from 1 to 100, but ends early if the number is a multiple of 10.
for h in range(1,100):
    if h % 10 == 0:
        print(h)
        break
    else:
        print(h)
#14. Free space. Do something creative. :)