# Filename: ass8.py
# Description: cheating vegas

import sys
sys.dont_write_bytecode = True

from ass8 import *

def main():
    d = {}
    d["cherries"] = 0
    d["BAR"] = 0
    d["7"] = 0
    d["space"] = 0
    total_winnings = 0
    spent = 100000
    for i in range(0, spent):
        bet = 1
        reels = pull()
        winnings = get_pay_multiplier(reels)
        total_winnings += winnings
        d[reels.get_str1()] += 1
        d[reels.get_str2()] += 1
        d[reels.get_str3()] += 1

    print("Money spent: %d" % spent)
    print("Money earned: %d" % total_winnings)
    print("Net earnings: %d" % (total_winnings - spent))
    print("")
    total_times = spent * 3
    for key in d:
        print("Times %s appeared: %d" %(key, d[key]))
        print("Percentage %s appeared: %.6f%%" % (key, 100*d[key]/(total_times)))
        print("")

    print("Exiting.")

if __name__ == "__main__":
    main()
