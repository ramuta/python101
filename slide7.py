__author__ = 'ramuta'

# Data structures

# List
""" You can add new entries, delete old ones """
some_list = ["Ana", "Jack", "Marfat", "Yago"]

for person in some_list:
    print person

some_list.append("Matej")

print some_list.index("Matej")

# Tuples
""" Similar to lists, but you cannot add new items (immutable).
A workaround is converting to list, adding new value and then converting back to tuple.
Or joining two tuples.
Tuples are good for grouping data, for examples coordinates (long,lat).
You can store different long-lat pairs in a list: [(89.32,123.53554), (45.2332, 115.23), (33.33, 22.22)]
"""
some_tuple = ("January", "February", "March", "April", "May")
print some_tuple

missing_tuple = ("June",)
some_tuple += missing_tuple
print some_tuple


# Dictionary
""" A hash table: key-value pairs. It is unordered (you shouldn't rely on your order). """
my_dict = {"key1": 13, "key2": "my value", "key3": True}
print my_dict

for item in my_dict:
    print my_dict[item]


# Task: Country-capital game
data = {
    "Slovenia": "Ljubljana",
    "Great Britain": "London",
    "Netherlands": "Amsterdam",
    "Spain": "Madrid"
    }

for item in data:
    answer = raw_input("What is the capital of %s? " % item)
    if answer == data[item]:
        print "Correct!"
    else:
        print "Wrong!"