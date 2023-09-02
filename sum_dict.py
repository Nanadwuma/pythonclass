# """
# #using the Counter Module
# from collections import Counter

# dict1 = {'a': 100, 'b': 200, 'c':300}  
# dict2 = {'a': 300, 'b': 200, 'd':400} 

# new_dict = Counter(dict1) + Counter(dict2)

# #print(new_dict)

# #assigne the two dictionaries and called the Counter() function on dict1 and dict2 
# new_dict = dict2  
# for i, j in dict1.items():  
#     if i in dict2:  
#         new_dict[i] = j + dict2[i]  
#     else:   
#         new_dict[i] = j  
# #print("The new dict is:", new_dict) 

# #initialized the dictionaries and the dict2 in the new_dict
# #run for loop using the items() method to the dict2.
# #checked if the key exists in dict1; if true, then add it with the value to the dict1; 
# # else assign as a key of new_dict

# dict3= {}  
# dict3.update(dict1)  
# dict3.update(dict2)  
# for i,j in dict1.items():  
#     for x,y in dict2.items():  
#         if i ==x:  
#             dict3[i] = j+y  
# #print(dict3) 

# dict3= {}  
# dict3.update(dict1)  
# dict3.update(dict2)  
# if x in dict2.keys():  
#     dict1[x]=dict1[x]+dict2[x]  
#     dict2.pop(x)  
  
# for d in (dict1,dict2):  
#     dict3.update(d)  
# print(dict3)

# """

# employee_salary = {
#     "EMP_101": {"name": "John", "salary":2000, "month": "June", "year": 2023},
#     "EMP_201": {"name": "James", "salary":1500, "month": "June", "year": 2023},
#     "EMP_301": {"name": "Kofi", "salary":6000, "month": "July", "year": 2023},
#     "EMP_401": {"name": "Yaya", "salary":5000, "month": "April", "year": 2021},
#     "EMP_501": {"name": "Felicia", "salary":10000, "month": "May", "year": 2021},
#     "EMP_801": {"name": "Ama", "salary":5500, "month": "June", "year": 2022},
# }

# # ASSIGNMENT
# # Sum the total of salaries for all the employees

# #Step 1: Know the data in the dict
# for id, emp_info in employee_salary.items():
#     print(emp_info)

# # Step2 :Know the salaries in the dict

# for id, emp_info in employee_salary.items():
#     # print(emp_info["salary"])
#     print(f"\nEmployee ID: {id} ")
#     for key in emp_info:
#         print(f"{key.title()}: {emp_info[key]}")

     
# #Step 2: Add all (sum) the salaries
# # total_salary = sum(employee["salary"] 
# #     for employee in employee_salary.values())

# # print("Total Salary of all Employees:", total_salary)

# print("--------------------------------------")
# #Assigne a variable to total salary
# total_salary = 0


# # Loop through to sum all salary up
# for employee_info in employee_salary.values():
#     total_salary += employee_info["salary"]
#     # total_salary =  total_salary + employee_info["salary"]

# # print(total_salary)
# # print("Total Salary of all Employees:", total_salary)

# #Assignment
# # Sum total salary of those in June 2023

# # sum_2023 = sum(employee["salary"] 
# # for employee in employee_salary.values() 
# # if employee["year"] == 2023)
# # print(sum_2023)

# # sum_june_2023 = sum(employee["salary"]
# # for employee in employee_salary.values(): 
# #     if employee["month"] == "June" and employee["year"] == 2023:
# # print(sum_june_2023)

# sum_june_2023 = sum(employee["salary"]
# for employee in employee_salary.values() 
#     if employee["month"] == "June" and employee["year"] == 2023)
# # print(sum_june_2023)


# # review
# _sum_june_2023 = 0
# _total_salary = 0
# for employee in employee_salary.values():
#     _total_salary += employee_info["salary"]
#     if employee["month"] == "June" and employee["year"] == 2023:
#         print(f"Name: {employee['name']} - {employee['salary']}")
#         _sum_june_2023 += employee["salary"]

# print(f"Total Salary for June 2023: {_sum_june_2023}") 
# print(f"Total Salary all Staff: {_total_salary}") 


# Assignment 5
# a list of dictionaries
countries_data = [
    {"country": "Ghana", "population":10000, "continent": "Africa"},
    {"country": "Nigeria", "population":20000, "continent": "Africa"},
    {"country": "Brazil", "population":70000, "continent": "South America"},
    {"country": "China", "population":500000, "continent": "Asia"},
]
# Get the total population in the countries_data
# Print the countries in Africa and their popluation
# Get the total of the polpulation of African countries
# What is the difference beteen the poluation of China and African countries

#STEPS: First of all, the data above is a List of Dictionaries
#1
#To get the total popuplation in the countries_data

#Step 1: Create a variable to store the total population
total_population = 0
total_population_africa = 0
population_china = 0

#Step 2: Loop through each dictionary in countries_data
for country_info in countries_data:
 
    total_population =  total_population + country_info["population"]
    #total_population += country_info["population"]

    if country_info["continent"] == "Africa":
        country_name = country_info["country"]
        population = country_info["population"]
        #print(f"Country: {country_name}, Population: {population}")
        print(f"{country_name},{population}")
        total_population_africa += country_info["population"]
    if country_info["country"] == "China":
        population_china = country_info["population"]

#Step 8: Calculate the difference
difference = population_china - total_population_africa

print("Total Population :", total_population)
print("Total Population of African Countries:", total_population_africa)
print("The difference between Population of China and African Countries:", difference)


#Challenges

# Had challenges with moving to the next step of code without repeating the for loop
# Had to repeat it to avoid errors. At some sessions, had to comment previous codes in order to avoid errors in current codes.

# Example
# From Step 6, if i dont repeat the for loop on line 166,which has already been stated in line 145, i get errors. 

# Again, 
# On line 175, if i dont repeat the variable, i get miscalulations in the total figure
