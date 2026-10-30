


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

attacers["lion"].update({"health" : int(input("what do u want the new health to be?"))})
attacers["Dokkaebi"].update({"health" : int(input("what do u want the new health to be?"))})
attacers["Amaru"].update({"health" : int(input("what do u want the new health to be?"))})
attacers["Solid Snake"].update({"health" : int(input("what do u want the new health to be?"))})
attacers["Sens"].update({"health" : int(input("what do u want the new health to be?"))})
print(attacers)

print("note u can only use their abilitys 2 times")

attacers["lion"].update({"health" : int(input("how many times do u want to use lions ability"))})
attacers["Dokkaebi"].update({"health" : int(input("how many times do u want to use how many times do u want to use dokkaebi ability ability"))})
attacers["Amaru"].update({"health" : int(input("how many times do u want to use amaru ability"))})
attacers["Solid Snake"].update({"health" : int(input("how many times do u want to use solid snake ability"))})
attacers["Sens"].update({"health" : int(input("how many times do u want to use senses ability"))})


