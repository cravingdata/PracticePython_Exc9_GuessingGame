import random

user_guess = int(raw_input("Guess a number between 1 and 9:  "))
print

random = random.randint(1, 9)

print "you guessed: %s" % user_guess
print "random #: %s" % random

print
def compare(a,b):
    if a < b:
        return "You guessed too high."
    elif a > b:
        return "You guessed too low."
    else:
        return "You guessed correctly! Nice job!"


print compare(random,user_guess)
