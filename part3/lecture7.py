# Dictionaries in Python
this_dictionary = {
    "car" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}
print(this_dictionary)
print(this_dictionary["car"])


this_dictionary1 = {
    "car" : True,
    "brands" : ["Ford","Toyota", "BMW"],
    "year" : 2022
}
print(this_dictionary1["brands"][1])

new_list = [
    {
        "car" : True,
        "brands" : ["Ford","Toyota", "BMW"],
        "year" : 2022
    },
    {
        "car" : False,
        "brands" : ["Ranger","Kluger", "X5"],
        "year" : 2022
    },
]
print(new_list[0]['car'])
print(new_list[0]['brands'][2])

new_dict = dict(car = 'Tesla')
print(new_dict)