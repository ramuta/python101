__author__ = 'ramuta'

d = lambda x: x**2
doubles = [d(x) for x in range(10)]
print [x for x in doubles if x % 2 == 0]