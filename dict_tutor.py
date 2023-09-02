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

'''
Assignment 3
'''


#  chagne care one brand to benz and model to c-lass

#  1. Print the old data
#  2. get cars
#  3. get car 1 from cars
#  4. change brand to benz and model to c-class of car_1
#  5. Print the new data

# Step: Printning the old data
# print("-> Old Data: ", personnel_data_dict)

# Getting cars data
# personnel_data_dict["cars"]
cars = personnel_data_dict["cars"]

# Get car_1 from cars
#print(cars["car_1"])
car_1 = cars["car_1"]

# change car_1 brand and model
car_1["brand"] = "Benz"
car_1["model"] = "C-Class"

# using update method to update
# car_1.update({"brand": "Benz", "model": "C-Class"})

# print the new data
# print("<- New Data: ", personnel_data_dict)



# Assignment
# Break down the steps
# Use the new variable declaration approach
# Add colour to car_1 and car_2
# Add year of manufacture to each car

# Step 1: Printning the old data
# print("=====> Old Data: ", personnel_data_dict)

# Step 2: Get cars data
# personnel_data_dict["cars"]
cars = personnel_data_dict["cars"]

#Step 3: Get car_1 from cars
#print(cars["car_1"])
car_1 = cars["car_1"]

#Step 4: Get car_2 from cars
#print(cars["car_2"])
car_2 = cars["car_2"]

#Step 5: Adding colour and year of manufacture to car_1 and car_2 using new variable declaration
car_1_colur = "White"
car_1_yr_of_manu = 2018

car_1["colour"] = "white"
car_1["yr_of_manu"] = 2018

car_2["colour"] = "black"
car_2["yr_of_manu"] = 2020
#print(car_2)

#Step 6: Print new data
# print("=====> New Data: ", personnel_data_dict)


"""
using loops and conditionals on dictionary
"""

employee_salary = {
    "EMP_101": {"name": "John", "salary":2000, "month": "June", "year": 2023},
    "EMP_215": {"name": "James", "salary":1500, "month": "June", "year": 2023},
    "EMP_362": {"name": "Kofi", "salary":6000, "month": "July", "year": 2023},
    "EMP_4": {"name": "Yaya", "salary":5000, "month": "April", "year": 2021},
    "EMP_51": {"name": "Felicia", "salary":10000, "month": "May", "year": 2021},
    "EMP_81": {"name": "Ama", "salary":5000, "month": "June", "year": 2022},
}

#total records
# print("Number of records: ", len(employee_salary))

#John salary
# print(employee_salary[1]["salary"])

# Get names of all employees in this dict
#Step 1: Go to the main folder
# print(employee_salary[1]["name"])
# print(employee_salary[2]["name"])
# print(employee_salary[3]["name"])
# print(employee_salary[4]["name"])
# print(employee_salary[5]["name"])
# print(employee_salary[6]["name"])

# in class assignment: Get names of all records in 2021

#print("Dict Items==> ", employee_salary.items())

for id, emp_info in employee_salary.items():
    # print(id)
    #if year = 2021, we can print or get values(names) in 2021
    #if emp_info["year"] == 2023:
     #print(emp_info["name"])
        
#if year = 2023, get names of those who were paid in June
#if emp_info["year"] == 2023:
    #if emp_info["year"] == 2023 and "June":
    #if emp_info["month"] == 2023 and "June":
    
    #if emp_info["month"]  == "June" and 2023:
    #if emp_info["month"] == "July" and 2021:
    #if emp_info["month"] == "May" and 2021:
   if emp_info["year"] == 2023 and emp_info["month"] == "June":
   
     #sum += emp_info["salary"]
     #print(sum)
     print(emp_info["name"])
    


#print(employee_salary.items())