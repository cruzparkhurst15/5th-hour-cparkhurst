#Name:
#Class: 5th Hour
#Assignment: HW5

#1. Print Hello World!
print ("hello mack")
#1. Create a list with 5 strings containing 5 different names in it.
name_list = ["lila", "mack", "jake", "camden", "ethan"]
#2. Append a new name onto the Name List.
name_list.append("bob")
#3. Print out the 4th name on the list.
print (name_list[3])
#4. Create a list with 4 different integers in it.
num_list=[3, 4,7, 11,]
#5. Insert a new integer into the 2nd spot and print the new list.
num_list.insert(1,5)
print (num_list)
#6. Sort the list from lowest to highest and print the sorted list.
num_list.sort()
print (num_list)
#7. Add the 1st three numbers on the sorted list together and print the sum.
num_list_sum=(num_list[0]+num_list[1]+num_list[2])
print (num_list_sum)
#8. Create a list with two strings, two variables, and too boolean values.
random_list=["mack","sammy",9,8,True,False]
#9. Create a print statement that asks the user to input their own index value for the list on #8.
print (random_list[int(input("enter index location"))])