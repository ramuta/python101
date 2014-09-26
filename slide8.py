__author__ = 'ramuta'


# Function
def sum_of_two_numbers(a, b):
    c = a + b
    return c

print sum_of_two_numbers(5, 3)


# Class and OOP.
""" Variables inside classes are already wrapped in
getter and setter - actually they are objects themselves.
"""
class Car():
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def fast_or_slow(self):
        if self.speed > 100:
            return "This car is fast!"
        else:
            return "This car is slower than your grandma..."

fiat = Car(brand="Fiat", speed=30)
ferrari = Car(brand="Ferarri", speed=200)

print fiat.brand + ". " + fiat.fast_or_slow()
print ferrari.brand + ". " + ferrari.fast_or_slow()


# import example
"""You can add import statement wherever inside the file you want"""
from datetime import datetime

print datetime.now()


# Task: convert guess Country-capital game to use OOP
class Country():
    def __init__(self, name, capital):
        self.name = name
        self.capital = capital

    def check_capital(self, guess):
        if self.capital == guess:
            return "Correct!"
        else:
            return "Wrong!"

countries = []
slovenia = Country("Slovenia", "Ljubljana")
spain = Country("Spain", "Madrid")
uk = Country("Great Britain", "London")
holland = Country("Netherlands", "Amsterdam")
countries.append(slovenia)
countries.append(spain)
countries.append(uk)
countries.append(holland)

for country in countries:
    answer = raw_input("What is the capital of %s? " % country.name)
    print country.check_capital(answer)