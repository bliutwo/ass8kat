# Filename: ass8.py
# Description: cheating vegas

import random

class TripleString():
   
   
  # intended class constants 
   MAX_LEN = 50
   MIN_LEN = 1
   DEFAULT_STRING = "(undefined)"

  

   # constructor method 
   def valid_string(self,s):
      result = type(s) == str 
      if (not result):
         return False 
      return (len(s) >= self.MIN_LEN and len(s) <= self.MAX_LEN) 
    
   def __init__(self,
                string1 = DEFAULT_STRING, string2 = DEFAULT_STRING,
                string3 = DEFAULT_STRING):
      if (self.valid_string(string1)):           
         self.string1 = string1
      else:
         self.string1 = self.DEFAULT_STRING

      if (self.valid_string(string2)):           
        self.string2 = string2
      else:
        self.string2 = self.DEFAULT_STRING
    
      if (self.valid_string(string3)):           
        self.string3 = string3
      else:
        self.string3 = self.DEFAULT_STRING

   # mutator ("set") methods -------------------------------

   def set_str1(self,string1):
      if self.valid_string(string1) == False:
         return False 
      else:
         self.string1 = string1 
      return True 
   def set_str2(self,string2):
      if self.valid_string(string2) == False:
         return False
      else:
         self.string2 = string2
         return True 
   def set_str3(self,string3):
      if self.valid_string(string3) == False:
         return False   
      else:
         self.string3 = string3
         return True
   # accessor ("get") methods -------------------------------
   def get_str1(self):
      return self.string1 
   def get_str2(self):
      return self.string2
   def get_str3(self):
      return self.string3

   # helper methods for entire class -----------------
   def display_everything(self):
      print(self.string1)
      print(self.string2)
      print(self.string3)

def old():
    l = []

    triple_string_1 = TripleString()
    triple_string_2 = TripleString('hi','hello','there')
    triple_string_3 = TripleString(12,'numbers','fun')
    triple_string_4 = TripleString('hello','world')

    l.append(triple_string_1)
    l.append(triple_string_2)
    l.append(triple_string_3)
    l.append(triple_string_4)

    print('First display of all objects:')
    count = 1
    for ts in l:
       print('String',count)
       ts.display_everything()
       print('')
       count +=1

    for ts in l: 
       ts.set_str1('asd;lkfajskldf')

    print('Second display of all objects:')
    count = 1
    for ts in l:
       print('String',count)
       ts.display_everything()
       print('')
       count +=1
    print('two explicit mutator tests:')
    print('Set for string2 of triple_string_1')
    if l[0].set_str2('summer'):
       print('Call is successful')
    else:
       print('Call failed')

    print('')
    print('Set for string2 of triple_string_2')
    if l[1].set_str2(100):
       print('Call is successful')
    else:
       print('Call failed')

    print('')
    print('Make two accessor calls to demonstrate that they work.')
    print('triple_str_2, string 1:',l[1].get_str1())
    print('triple_str_1, string 2:',l[0].get_str2())

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

def get_pay_multiplier(reels):
    pass

def display(reels, winnings):
    pass

def main():
    # old()
    # limit = 100
    # print(random.randrange(limit))

    bet = get_bet()

    while bet != 0:
        reels = pull()
        
        # reels.display_everything()
        # TODO: display stuff
        bet = get_bet()

    print("Exiting.")

if __name__ == "__main__":
    main()
