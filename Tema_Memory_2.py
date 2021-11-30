import csv
import os

""" citire fisier """

# import csv
#
# with open('data_cars.csv', 'r') as fisierul_meu:
#     rows = csv.reader(fisierul_meu)
#     for row in rows:
#         print(row)

path = 'D:/output_data/'
directory = "output_data"

try:
    if os.path.exists(path):
        print("Fisierul Exista!")
    else:
        os.mkdir(path)
        print("Fisierul a fost creat!")
except:
    pass


cars =  [
 #        ('Brand', 'Model', 'An', 'hp', 'price'),
         ('Opel', 'Astra', 2002, 101, 800),
         ('Mazda', '6', 2012, 120, 600),
         ('Ford', 'Focus', 2009, 105, 4000),
         ('Dacia', 'Logan', 2005, 75, 5000),
         ('Dacia', 'Sandero', 2010, 200, 6000)

]

print("('Brand', 'Model', 'An', 'hp', 'price')\n")

slow_cars = lambda data:data[3] < 120
slow_cars1 = list(filter(slow_cars, cars))

for i in slow_cars1:
    print(i)
print(" ---------SLOW CARS------------------\n")


fast_cars = lambda data:data[3] >= 160
fast_cars1 = list(filter(fast_cars, cars))

for j in fast_cars1:
    print(j)
print(" ---------FAST CARS------------------\n")

sport_cars = lambda data:data[3] >= 180
sport_cars1 = list(filter(sport_cars, cars))

for i in sport_cars1:
    print(i)
print(" ---------SPORT CARS------------------\n")


# -------------------------------------------------------------------

cheap_cars = lambda data:data[4] < 1000
cheap_cars1 = list(filter(cheap_cars, cars))

for i in cheap_cars1:
    print(i)
print(" ---------CHEAP CARS------------------\n")


medium_cars = lambda data:data[4] >= 1000
medium_cars1 = list(filter(medium_cars, cars))

for j in medium_cars1:
    print(j)
print(" ---------MEDIUM CARS------------------\n")

expensive_cars = lambda data:data[4] > 5000
expensive_cars1 = list(filter(expensive_cars, cars))

for i in sport_cars1:
    print(i)
print(" ---------EXPENSIVE CARS------------------\n")


with open(os.path.join(path, 'Slow Cars.csv'), 'w') as my_file:
    my_file.write(str(list(slow_cars1)))

with open(os.path.join(path, 'Fast Cars.csv'), 'w') as my_file:
    my_file.write(str(list(fast_cars1)))

with open(os.path.join(path, 'Sport Cars.csv'), 'w') as my_file:
    my_file.write(str(list(sport_cars1)))

with open(os.path.join(path, 'Expensive Cars.csv'), 'w') as my_file:
    my_file.write(str(list(expensive_cars1)))

with open(os.path.join(path, 'Medium Cars.csv'), 'w') as my_file:
    my_file.write(str(list(medium_cars1)))

with open(os.path.join(path, 'Cheap Cars.csv'), 'w') as my_file:
    my_file.write(str(list(cheap_cars1)))