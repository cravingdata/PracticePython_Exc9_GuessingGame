#description: in this game, user plays until s/he declares game should end.
#the game also lets user know how many times user played.

import random


def compare(a,b):
    if a < b:
        return "You guessed too high."
    elif a > b:
        return "You guessed too low."
    else:
        return "You guessed correctly! Nice job!"

random = random.randint(1, 9)
num = 1

while_loop = True
while num >= 1:

    user_guess = int(raw_input("Guess a number between 1 and 9:  "))
    print

    print "you guessed: %s" % user_guess
    print "random #: %s" % random
    print
    print compare(random,user_guess)
    print
    end_game = raw_input("Do you want to end game? Type 'Y' for yes and 'N' for no: ")
    print

    if end_game == 'No' or end_game == 'N' or end_game == 'n':
        while_loop = True
        num = num + 1
    elif end_game == 'Yes' or end_game == 'Y' or end_game =='y':
        while_loop = False
        break


print "You've played this game %s times." % num
