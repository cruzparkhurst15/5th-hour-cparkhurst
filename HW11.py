#Name:Cruz Parkhurst
#Class: 5th Hour
#Assignment: HW11
import random as r

#1. Print "Hello World!"
print("hello world")
#2. Create a list with three variables that each randomly generate a number between 1 and 100
List=[r.randint(1,100),r.randint(1,100),r.randint(1,100)]
#3. Print the list.
print(List)
#4. Create an if statement that determines which of the three numbers is the highest and prints the result.
if List[0]>List[1] and List[0]>List[2]:
    print(f"{List [0]} is gerater than 1 and 2")
    num= List[0]
elif List[1]>List[0] and List[1]>List[2]:
    print(f"{List [1]} is smaller than 2 and 3")
    num= List[1]
elif List[2]>List[0] and List[2]>List[1]:
    print(f"{List[2]} is gerater than 1 and 3")
    num= List[2]

#5. Tie the result (the largest number) from #4 to a variable called "num".

#6. Create a nested if statement that prints if num is divisible by 2, divisible by 3, both, or neither. if i >= 2:
if num % 2 == 0:
    if num % 3 == 0:
        print(f"{num} is divisible by 3 and 2")
    else:
        print(f"{num} is is divisible by 2`")
else:
    if num % 3 == 0:
        print(f"{num} is divisible by 3 ")
    else:
        print(f"{num} is not divisible by 3 or 2  ")
