#Name:cruz parkhurst
#Class: 5th Hour
#Assignment: HW8


#1. Import the "random" library
import random as r
from random import random

#2. print "Hello World!"
print("Hello mack")
#3. Create three different variables that each randomly generate an integer between 1 and 10
seven=r.randint(1,10)
headphone=r.randint(1,10)
sonic=r.randint(1,10)

#4. Print the three variables from #3 on the same line.
print(seven,headphone,sonic)
#5. Add 2 to the first variable in #3, Subtract 4 from the second variable in #3, and multiply by 1.5 the third variable in #3.
seven= seven+2
headphone=headphone-4
sonic=sonic*1.5
#6. Print each result from #5 on the same line.
print(seven,headphone,sonic)
#7. Create a list containing four variables that each randomly generate an integer between 1 and 6
love=[r.randint(1,6),r.randint(1,6),r.randint(1,6),r.randint(1,6)]
#8. Sort the list in #7 and print it.
love.sort()
print(love)
#9. Add together the highest three numbers in the list from #7 and print the result.
job=love[1]+love[2]+love[3]
print(job)
#10. Create a list with 5 names of other students in this class and print the list.
studen_nam=["lila","neely","wyatt","gavin", "echo"]
#11. Shuffle the list in #10 and print the list again.
r.shuffle(studen_nam)
print(studen_nam)
#12. Print a random choice from the list of names from #10.