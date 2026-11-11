#Name:Cruz parkhurst
#Class: 5th Hour
#Assignment: HW15
import time

#1. Create a for loop with variable i that counts down from 5 to 1 and then prints "Hello World!"
#at the end.
for i in range(5,0,-1):
    time.sleep(0.4)
    print(i)
#2. Create a for loop that counts up and prints only even numbers between 1 and 30.
for j in range(0,31,2):
    time.sleep(0.4)
    print(j)
#3. Create a for loop that prints from 1 to 30 and continues (skips the number) if the number is
#divisible by 3.
for h in range(31):
    if h % 3 == 0:
        time.sleep(0.4)
        print(h)
#4. Create a for loop that prints 5 different animals from a list.
animals = ['dog', 'cat', 'bird','Parastratiosphecomyia stratiosphecomyioides','sloth']
for animal in animals:
    print(animal)
#5. Create a for loop that spells out a word you input backwards.
#(HINT: Google "How to reverse a string in Python")
txt= ('Supercalifragilisticexpialidocious')
for d in input('give me a word ')[::-1]:
    time.sleep(0.4)
    print(d)

#6. Create a list containing 10 integers of your choice and print the list.
sin= [12,11,4,45,5,36,89,55,66,777]
print(sin)
#7. Create two empty variables named evenNumbers and oddNumbers.
evenNumbers= 0
oddNumbers= 0
#8. Make a loop that counts the number of even and odd numbers in the list, and prints the
#result after the loop.
for number in sin:
    if number % 2 == 0:
        evenNumbers +=1
    else:
        oddNumbers+=1
print(evenNumbers,oddNumbers)



#9. Create a variable that asks the user for an integer and an empty integer variable.
num = int(input('give me a number '))
list_empty = 1
#10. Create a loop with a range from 1 to the number the user input. Use the loop to find the
#factorial of that number and print the result. A factorial of a number is that number multiplied
#by every number before it until you reach 1. (For example: 5! is 5 x 4 x 3 x 2 x 1 = 120)
for bob in range(1, num +1):
    list_empty *= bob
print(list_empty)