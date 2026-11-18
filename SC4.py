#Name:cruz parkhurst
#Class: 6th Hour
#Assignment: SC4

#You have been transferred to a new team working on a mobile game that allows you to dress up a
#model and rate other models in a "Project Runway" style competition.

#They want to start prototyping the rating system and are asking you to make it.
#This prototype needs to allow the user to input the number of players, let each player rate
#a single model from 1 to 5, and then give the average score of all of the ratings

player_num = int(input('How many players are playing?'))
player_num = player_num - 1
r=0

for i in range(player_num):
    g=True
    while g==True:
        choice = int(input('rate 1-5:'))
        if 1 <= choice <= 5:
            r = r+ choice
            g = not g
            g = False
        else:
            print('invalid choice')

b= r/player_num
print(b)
