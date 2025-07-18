# Lista simulada de países
countries = ['Finland', 'Iceland', 'Thailand', 'Switzerland', 'Germany', 'Canada']

# Filtrar países que contienen 'land'
for country in countries:
    if 'land' in country:
        print(country)
#Frutas 
fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = []

for i in range(len(fruits) - 1, -1, -1):
    reversed_fruits.append(fruits[i])
#CIUDADES   
print("Frutas invertidas:", reversed_fruits)
countries_data = [
    {'name': 'Finland', 'languages': ['Finnish', 'Swedish'], 'population': 5540720},
    {'name': 'Ethiopia', 'languages': ['Amharic'], 'population': 120812698},
    {'name': 'India', 'languages': ['Hindi', 'English'], 'population': 1400000000},
    {'name': 'USA', 'languages': ['English'], 'population': 331000000},
    {'name': 'Nigeria', 'languages': ['English'], 'population': 206000000},
    {'name': 'Brazil', 'languages': ['Portuguese'], 'population': 214000000},
    {'name': 'Russia', 'languages': ['Russian'], 'population': 145000000},
    {'name': 'Mexico', 'languages': ['Spanish'], 'population': 126000000},
    {'name': 'Germany', 'languages': ['German'], 'population': 83000000},
    {'name': 'France', 'languages': ['French'], 'population': 67000000},
]
