""" partea 1 - tema"""

import csv
import os
import copy

cars = [{
    "id": lambda: 1,
    "brand": "Opel",
    "model": "Astra",
    "hp": 110,
    "price": 1000
}, {
    "id": lambda: 1,
    "brand": "Wolkswagen",
    "model": "Tiguan",
    "hp": 160,
    "price": 2000
}, {
    "id": lambda: 1,
    "brand": "Dacia",
    "model": "Logan",
    "hp": 80,
    "price": 500
}, {
    "id": lambda: 1,
    "brand": "Audi",
    "model": "A4",
    "hp": 170,
    "price": 3000
}, {
    "id": lambda: 1,
    "brand": "Mercedes",
    "model": "AMG",
    "hp": 190,
    "price": 7000
}]


def slow_cars(cars):
    update_list = copy.deepcopy(cars)
    if update_list["hp"] < 120:
        return update_list

update_list = filter(slow_cars, cars)
print('Slow Cars', list(update_list))

def fast_cars(cars):
    update_list2 = copy.deepcopy(cars)
    if update_list2["hp"] >= 120 and update_list2["hp"] < 180:
        return update_list2

update_list2 = filter(fast_cars, cars)
print('Fast Cars', list(update_list2))

def sport_cars(cars):
    update_list3 = copy.deepcopy(cars)
    if update_list3["hp"] >= 180:
        return update_list3

update_list3 = filter(sport_cars, cars)
print('Sport Cars', list(update_list3))


def cheap_cars(cars):
    price_list = copy.deepcopy(cars)
    if price_list["price"] < 1000:
        return price_list

price_list = filter(slow_cars, cars)
print('Cheap Cars', list(price_list))


def medium_cars(cars):
    price_list1 = copy.deepcopy(cars)
    if price_list1["price"] >= 1000 and price_list1["price"] < 5000:
        return price_list1

price_list1 = filter(medium_cars, cars)
print('Medium Cars', list(price_list1))

def expensive_cars(cars):
    price_list3 = copy.deepcopy(cars)
    if price_list3["price"] >= 5000:
        return price_list3

price_list3 = filter(expensive_cars, cars)
print('Expensive Cars', list(price_list3))


"""partea 2 - tema"""

with open('input.csv', 'r') as fisierul_meu:
    rows = csv.reader(fisierul_meu)
    for row in rows:
        print(row)


"""creare director si fisiere"""

directory = "output_data"
path = 'D:/output_data/'
os.mkdir(path)


Slow_cars = 'Slow_cars.json'
Fast_cars = 'Fast_cars.json'
Sport_cars = 'Sport_cars.json'
Cheap_cars = 'Cheap_cars.json'
Medium_cars = 'Medium_cars.json'
Expensive_cars = 'Expensive_cars.json'
Ford = 'Ford.json'


with open(os.path.join(path, Slow_cars), 'w') as my_file:
    my_file.write(str(update_list))


with open(os.path.join(path, Fast_cars), 'w') as my_file:
    my_file.write(str(update_list2))


with open(os.path.join(path, Sport_cars), 'w') as my_file:
    my_file.write(str(update_list3))

with open(os.path.join(path, Cheap_cars), 'w') as my_file:
    my_file.write(str(price_list))


with open(os.path.join(path, Medium_cars), 'w') as my_file:
    my_file.write(str(list))


with open(os.path.join(path, Expensive_cars), 'w') as my_file:
    my_file.write(str(price_list1))


with open(os.path.join(path, Ford), 'w') as my_file:
    my_file.write(str(price_list3))
