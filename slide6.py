__author__ = 'ramuta'

# variables
num = 6
name = "matej"
some_boolean = True


# print, input
print name

"""
Use raw_input instead of input.
Input takes your input as a command (and is unsafe), while raw_input takes it as a string.
"""
question = raw_input("What is you favourite food? ")
print "Your favourite food is: " + question


# if statements (indentation is very important!!!)
if num > 0:
    print "Positive integer"
else:
    print "Negative integer"


# loops
for number in range(10):
    print number

print "----"

while num < 10:
    print num
    num += 1

print "----"


# Task: Guess the secret number game
from random import randint

secret = randint(1, 10)
guess = 0

while guess != secret:
    guess = int(raw_input("What is the secret number? "))
    if guess == secret:
        print "Yaaaay! That's correct, %s" % secret
    else:
        print "Sorry, %s is not a correct number. Please try again." % guess

print "The end. Run the program again to start a new game."