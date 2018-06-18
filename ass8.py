# Filename: ass8.py
# Description: cheating vegas

import sys
sys.dont_write_bytecode = True

import random
from TripleString import *

def get_bet():
    prompt = "Input amount to bet (0 to 50): "
    user_input = int(input(prompt))
    error = "Invalid amount."
    while user_input < 0 or user_input > 50:
        print(error)
        user_input = int(input(prompt))
    return user_input

def rand_string():
    limit = 100
    n = random.randrange(limit)
    if n >= 0 and n < 40:
        return "cherries"
    elif n >= 40 and n < 78:
        return "BAR"
    elif n >= 78 and n < 93:
        return "7"
    else:
        return "space"

def pull():
    ts = TripleString()
    ts.set_str1(rand_string())
    ts.set_str2(rand_string())
    ts.set_str3(rand_string())
    return ts

# reels is of type TripleString
# returns 0, 5, 15, 30, 50, 100
def get_pay_multiplier(reels):
    if reels.get_str1() == "cherries" and reels.get_str2() == "cherries" and reels.get_str3() == "cherries":
        return 30
    elif reels.get_str1() == "BAR" and reels.get_str2() == "BAR" and reels.get_str3() == "BAR":
        return 50
    elif reels.get_str1() == "7" and reels.get_str2() == "7" and reels.get_str3() == "7":
        return 100
    elif reels.get_str1() == "cherries" and reels.get_str2() == "cherries" and reels.get_str3() != "cherries":
        return 15
    elif reels.get_str1() == "cherries" and reels.get_str2() != "cherries":
        return 5
    else:
        return 0

def display(reels, winnings):
    print("%s\t%s\t%s" % (reels.get_str1(), reels.get_str2(), reels.get_str3()))
    if winnings > 0:
        print("congrats, you won $%d" % winnings)
    else:
        print("sorry - you lost")


def main():
    bet = get_bet()

    while bet != 0:
        reels = pull()
        winnings = bet * get_pay_multiplier(reels)
        display(reels, winnings)
        print("")
        bet = get_bet()

    print("Exiting.")

if __name__ == "__main__":
    main()
