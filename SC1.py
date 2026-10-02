#Name:Cruz parkhurst
#Class: 5th Hour
#Assignment: Scenario 1

#Scenario 1:
#You are a programmer for a fledgling game developer. Your team lead has asked you
#to create a nested dictionary containing five enemy creatures (and their properties)
#for combat testing. Additionally, the testers are asking for a way to input changes
#to the enemy's damage values for balancing, as well as having it print those changes
#to confirm they went through.

#Other than damage which is required, it is up to you to decide what properties are
#important and the theme of the game.
attacers={
    "lion" : {
        "health" : 125,
        "damage" : 25,
        "ability": "EE-ONE-D"

    },"Dokkaebi" : {
        "health" : 125,
        "damage" : 25,
        "ability" : "Jegeo Payload"

    },"Amaru" : {
        "health" : 125,
        "damage" : 25,
        "ability" : "Garra Hook"

    },"Solid Snake" : {
        "health" : 125,
        "damage" : 25,
        "ability" : "SOLITON RADAR MK III"

    },"Sens" : {
        "health" : 125,
        "damage" : 25,
        "ability" : "R.O.U. Projector System"

    },

    }
print(attacers)
attacers["lion"].update({"damage" : int(input("what do u want the new damage to be?"))})
attacers["Dokkaebi"].update({"damage" : int(input("what do u want the new damage to be?"))})
attacers["Amaru"].update({"damage" : int(input("what do u want the new damage to be?"))})
attacers["Solid Snake"].update({"damage" : int(input("what do u want the new damage to be?"))})
attacers["Sens"].update({"damage" : int(input("what do u want the new damage to be?"))})
print (attacers)