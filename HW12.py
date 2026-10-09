#Name:cruz parkhurst
#Class: 5th Hour
#Assignment: HW12


#1. Print Hello World!
print ("Hello World")
#2. Create three different boolean variables named wifi, login, and admin.
wifi = True
login= True
admin= False
#3. Create a separate integer variable that denotes the number of times
#someone with admin credentials has logged in.
logged_in = 0
#4. Create a nested if statement that checks to see if wifi is true,
#login is true, and admin is true. If they are all true, print a
#welcome message and increase the integer variable by one. If one of them
#is false, print an error message telling them which one they are "missing".
if wifi == True:
    if login == True:
        if admin == True:
            print("Welcome in")
            logged_in += 1
        else :
            print("error admin is missing")
    else :
        print("error login is missing")
else:
    print("error wifi is missing")
