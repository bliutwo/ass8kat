# Filename: TripleString.py
# Description: contains the class TripleString

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


