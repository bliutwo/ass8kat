# Here is sample answer #2
from timeit import default_timer as timer

def makeDict(input_file_name):
   with open(input_file_name, 'r', encoding = 'utf-8') as f:
      dict_list = f.readlines()
      index = 0
      while index < len(dict_list):
         dict_list[index] = dict_list[index].rstrip('\n')
         index += 1
   keys = (x for x in range(1,1001))
   return dict(zip(keys, dict_list))

en_dict = makeDict("1kwords.en.txt")
sp_dict = makeDict("1kwords.sp.txt")
gr_dict = makeDict("1kwords.gr.txt")

dict_language = {"en": en_dict, "sp": sp_dict, "gr": gr_dict}

def translate(fm, to, word):
   if fm not in dict_language.keys():
      return("from is not a valid language code.")
   elif to not in dict_language.keys():
      return("to not a valid language code.")
   else:
      for i in range(1,1001):
         if fm == to:
            return( word )
         if word not in dict_language[fm].values():
            return("The word you want to look up is not in the dictionary.")
         if dict_language[fm][i] == word:
            return(dict_language[to][i])

def func_to_measure():
    spbee = translate("gr","sp", "μέλισσα")
    translate("sp","en", spbee)
    translate("en","sp", "heart")
    translate("en","gr", "heart")
    translate("en","gr", "diegetic")
    translate("gr", "en", "μέλισσα")
    spneck = translate("en", "sp", "neck")
    translate("en", "gr", "neck")
    translate("sp", "gr", spneck)
    translate("en", "sp", "beauty")

print(translate("en", "gr", "light"))
print(translate("en", "sp", "light"))
print(translate("sp", "en", "momento"))
print(translate("sp", "gr", "momento"))
print(translate("gr", "en", "πολλαπλασιάστε"))
print(translate("gr", "sp", "πολλαπλασιάστε"))

print(translate("en", "gr", "giraffe"))


spbee = translate("gr","sp", "μέλισσα")
print(spbee)
print(translate("en","sp", "heart"))
print(translate("en","gr", "heart"))
print(translate("en","gr", "diegetic"))
print(translate("gr", "en", "μέλισσα"))

spneck = translate("en", "sp", "neck")
print(translate("en", "gr", "neck"))
print(translate("sp", "gr", spneck))
print(translate("en", "sp", "beauty"))

print("starting timer")
start = timer()
for i in range(1000):
    func_to_measure()
end= timer()

elapsed = end - start
print("10000 words translated in", elapsed, "secs")
