#Name:Cruz Parkhurst
#Class: 5th Hour
#Assignment: HW13
print("Welcome to HW13")
#1. Import the random function
import random as r
#2. Create a variable called 'temp' that randomly generates a number between 1 and 30

temp= r.randint(1,30)
print(temp)



#3. Go to the link below and convert the code into pseudocode in comments, then code the flowchart completely:
#https://adacomputerscience.org/images/content/computer_science/design_and_development/program_design/figures/ad
# a_cs_design_flow_ifelseif.svg

#if temp is gerater than 20
    #print its hot
#if temp is gerater than 10
    #print its mild
#else its cold
#print thank you
if temp > 20:
    print("The temperature is too high")
elif temp > 10:
    print("The temperature is mild")
else :
    print("The temperature is cold")
print("Thank you")