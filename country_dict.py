# a list of dictionaries
countrys_data = [
    {"country": "Ghana", "population": 10000, "continent": "Africa"},
    {"country": "Nigeria", "population": 20000, "continent": "Africa"},
    {"country": "Brazil", "population": 70000, "continent": "South America"},
    {"country": "China", "population": 500000, "continent": "Asia"},
]

# Get the total population in the countrys_data
# Print the countries in Africa and their popluation
# Get the total of the polpulation of African countries
# What is the difference beteen the poluation of China and African countries

# 1. loop through countries data and sum all popluation
# declare total_popluation variable
total_popluation = 0
total_popluation_africa = 0
difference_china_africa = 0
for country in countrys_data:
    # Sum total population
    total_popluation += country["population"]

    # get african countries,their population and sum total population
    if country["continent"] == "Africa":
        print(f"{country['country']} - {country['population']}")
        total_popluation_africa += country["population"]

    # Get the population of chine and subtracet total population of africa  countries
    if country["country"] == "China":
        difference_china_africa = country["population"] - total_popluation_africa

print(f"Total Population: {total_popluation}")
print(f"Total Population of African Countries: {total_popluation_africa}")
print(f"Difference between China and Africa population: {difference_china_africa}")
