__author__ = 'ramuta'

# Bonus: the "weird" stuff

# Doing lists the standard way:
my_list = []

for num in range(10):
    my_list.append(num)

print my_list

# List comprehensions - another way of populating lists
new_list = [num for num in range(10)]
print new_list

print "----"

# lambda functions (nameless/unnamed/anonymous functions)

# ordinary way
def doubles(x):
    y = x**2
    return y

print doubles(5)

# lambda way
d = lambda x: x**2

print d(5)