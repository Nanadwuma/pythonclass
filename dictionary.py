# '''
# # Access nana's brain using dot notation=> nana.haead.brain
# dictionary stores data in key and value pairs;
# key 1, [], (), {}
#  in ther languages, a dictiioney is called json {} 
#  api = aplication programming/program interrface
# a_dict = {}
# '''

# personnel_data_dict = {
#     # "key" : "value" or value
#     "name": "Kofi",
#     "age": 21,
#     "date_of_birth": "09-07-1952",
#     "fruits": ["Banana", "Orange"],
#     "cars": {
#         "car_1": {
#             "brand": "Toyota",
#             "model": "Yaris"
#         },
#          "car_2": {
#             "brand": "Hyndai",
#             "model": "Sonata"
#         }
#     }
#     }

# # Accessing items in a dict

# # dict_name["key"] dict_name.get("key")
# # print(personnel_data_dict["name"])

# # finding the number of records in the dict
# # print(len(personnel_data_dict))

# # Update the age of Kofi
# # 1. Know the outcome of what i want to do age = 71
# # 2. get the existing age from the dictionary
# # 3. assign the new age to to the age key
# # 4.show me the old data and the new data
# # old_age = personnel_data_dict["age"]
# # new_age = 71
# #print("-> Old Data: ", personnel_data_dict)
# #personnel_data_dict["age"] = 71
# #print("<- New Data: ", personnel_data_dict)

# # update the date of bith
# # Update the date of birth to 1/1/2002
# # get the existing date of birth from the dictionary
# # assign the new date of birth to the date of birth key
# # show old and new data

# #print("-> Old Data: ", personnel_data_dict)
# #personnel_data_dict["date_of_birth"] = "01-01-2002"
# #print("<- New Data: ", personnel_data_dict)


# #print(personnel_data_dict["cars"])
# #print(cars["car1"])

# # How to access a dict from a dict                #Assignment
# personnel_data_dict = {
#     # "key" : "value" or value
#     "name": "Kofi",
#     "age": 21,
#     "date_of_birth": "09-07-1952",
#     "fruits": ["Banana", "Orange"],
#     "cars": {
#         "car_1": {
#             "brand": "Toyota",
#             "model": "Yaris"
#         },
#          "car_2": {
#             "brand": "Hyndai",
#             "model": "Sonata"
#         }
#     }
#     }
# print(personnel_data_dict["cars"]["car_1"])



# # Practice - Dictionary
# this_dict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# #print(this_dict["year"])
# print(len(this_dict))

# #Get Key

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# #x = car.keys()
# y = car.values()

# x = car.items()

# print(x) #before the change

# #ADD NEW ITEM TO DICT
# car["color"] = "white"

# #print(x) #after the change
# #print(y)


# # IF A KEY EXIST IN A DICT
# if "model" in car:
#     print("Yes, model is one of the keys in car")

# #CHANGE VALUES
# #car["year"] = 2018
# print(car)

# # UPDATE DICT
# car.update({"year" : 2022})
# print(car)

# # ADDING ITEMS
# car["type"] = "4x4"
# print(car)

# #REMOVING ITEMS
# #car.pop("model")  # The pop() method removes the item with the specified key name
# car.popitem()     #The popitem() method removes the last inserted item
# del car ["year"]  #The del keyword removes the item with the specified key name
# #del car          # this will cause an error because the dictionary "car" no longer exists
# #car.clear()      #The clear() method empties the dictionary
# print(car)

# # LOOP DICTIONARY
# #You can loop through a dictionary by using a for loop
# for x in car:
#     print(x)   #Print all key names in the dictionary, one by one

# for x in car:
#     print(car[x]) #Print all values in the dictionary, one by one:

# # Value method #use the values() method to return values of a dictionary
# for x in car.values():
#   print(x)      

# # Key method #use the key() method to return values of a dictionary
# for x in car.keys():
#   print(x)

# # Both key and value # Loop through both keys and values, by using the items() method
# for x, y in car.items():
#   print(x, y)

# #COPY A DICTIONAY
# #Make a copy of a dictionary with the copy() method
# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# mycar = car.copy()
# #print(mycar)

# #Make a copy of a dictionary with the dict() function
# mycar = dict(car)
# print(mycar)


# #NESTED DICTIONARY
# #Create a dictionary that contain three dictionaries

# myfamily = {
#   "sib1" : {
#     "name" : "Rose",
#     "year" : 2000
#   },
#   "sib2" : {
#     "name" : "Linda",
#     "year" : 2005
#   },
#   "sib3" : {
#     "name" : "Connie",
#     "year" : 2011
#   }
# }

# print(myfamily)

# # Create three dictionaries, then create one dictionary that will contain the other three dictionaries:

# child1 = {
#     "name" : "Kofi",
#     "year" : 2000
#   },
# child2 = {
#     "name" : "Ama",
#     "year" : 2005
#   },
# child3 = {
#     "name" : "Prince",
#     "year" : 2011
#   }
# mychildren = {
#    "child1" : child1,
#    "child2" : child2,
#    "child3" : child3
# }
# print(mychildren)

# #ACCESS ITEMS IN A NESTED DICT
# # use the name of the dictionaries, starting with the outer dictionary to access items from a dictionary
# myfamily = {
#   "sib1" : {
#     "name" : "Rose",
#     "year" : 2000
#   },
#   "sib2" : {
#     "name" : "Linda",
#     "year" : 2005
#   },
#   "sib3" : {
#     "name" : "Connie",
#     "year" : 2011
#   }
# }
# print(myfamily["sib3"]["year"])

# '''
# Dictionary Methods
# Python has a set of built-in methods that you can use on dictionaries.

# Method	- Description
# clear()	- Removes all the elements from the dictionary
# copy()	- Returns a copy of the dictionary
# fromkeys()	- Returns a dictionary with the specified keys and value
# get()	- Returns the value of the specified key
# items()	- Returns a list containing a tuple for each key value pair
# keys()	- Returns a list containing the dictionary's keys
# pop()	- Removes the element with the specified key
# popitem()	- Removes the last inserted key-value pair
# setdefault()	- Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	- Updates the dictionary with the specified key-value pairs
# values()	- Returns a list of all the values in the dictionary
# '''

# #ASSIGNMENT

# # How to access a dict from a dict
# personnel_data_dict = {
#     # "key" : "value" or value
#     "name": "Kofi",
#     "age": 21,
#     "date_of_birth": "09-07-1952",
#     "fruits": ["Banana", "Orange"],
#     "cars": {
#         "car_1": {
#             "brand": "Toyota",
#             "model": "Yaris"
#         },
#          "car_2": {
#             "brand": "Hyndai",
#             "model": "Sonata"
#         }
#     }
#     }
# print(personnel_data_dict["cars"]["car_2"]["model"])



# Update the brand and model of car_1
# 1. Know the outcome of what i want to do ie brand : benz , model: c class
# 2. get the existing brand of cars from the dictionary
# 3. assign the new brand and model to the car_1 key
# 4.show the old data and the new data
# old_brand = personnel_data_dict["cars"]
# old_model = personnel_data_dict["cars"]
# new_brand = benz
# new_model = c class

personnel_data_dict = {
    # "key" : "value" or value
    "name": "Kofi",
    "age": 21,
    "date_of_birth": "09-07-1952",
    "fruits": ["Banana", "Orange"],
    "cars": {
        "car_1": {
            "brand": "Toyota",
            "model": "Yaris"
        },
         "car_2": {
            "brand": "Hyndai",
            "model": "Sonata"
        }
    }
}

print("----> Old Data: ", personnel_data_dict)

new_brand = "benz"
new_model = "c class"

personnel_data_dict["cars"]["car_1"]["brand"] = new_brand
personnel_data_dict["cars"]["car_1"]["model"] = new_model

print("----> New Data: ", personnel_data_dict)

#print(old_brand)
#print(old_model)

# 
# Please whatsapp me when you return





