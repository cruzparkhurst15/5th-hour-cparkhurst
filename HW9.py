#Name:Cruz parkhurst
#Class: 5th Hour
#Assignment: HW9

#1. Print Hello World!
print("Hello Coach Mack")
#2. Create a dictionary with 3 keys and a value for each key. One of the keys must have a value with a list containing
#three numbers inside.
Cruzs_truck_details= {
    "brand": "F-150",
    "model": "ford",
    "year":[2003,2002,2004]
}

#3. Print the keys of the dictionary from #2.
print(Cruzs_truck_details.keys())

#4. Print the values of the dictionary from #2
print(Cruzs_truck_details.values())
#5. Print one of the three numbers from the list by itself
print(Cruzs_truck_details["year"][1])
#6. Using the update function, add a fourth key to the dictionary and give it a value.
Cruzs_truck_details.update({"engine" : "v8"})

#7. Print the entire dictionary from #2 with the updated key and value.
print(Cruzs_truck_details)
#8. Make a nested dictionary with three entries containing the name of another classmate and two other pieces of information
#within each entry.
fifth_hour_class = {
    "student_1" : {
        "Name" : "lila",
        "Grade" : 9,
        "Sport" : False,
    },
    "student_2" : {
        "Name" : "neely",
        "Grade" : 12,
        "Sport" : True,
    },
    "student_3" : {
        "Name" : "jake",
        "Grade" : 10,
        "Sport" : True,
    },
}
#9. Print the names of all three classmates on the same line.
print(fifth_hour_class["student_1"]["Name"], fifth_hour_class["student_2"]["Name"], fifth_hour_class["student_3"]["Name"])
#10. Use the pop function to remove one of the nested diction01aries inside and print the full dictionary from #8.
fifth_hour_class.pop("student_1")
print(fifth_hour_class)