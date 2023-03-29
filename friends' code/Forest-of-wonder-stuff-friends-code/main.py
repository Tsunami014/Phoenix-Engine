import json
import random
import time

def Voicelines():
  print('Vaules')
#It is chosing map
mapchoice=int(input("Chose a map. Type 1 for Ancient Egypt, Type 2 for Tech Labs and Type 3 for Forest.\n" ))
if mapchoice==1:
    print("Loading Map- Ancient Egypt")
elif mapchoice==2:
     print("Loading Map- Tech Labs")
elif mapchoice==3:
      print("Loading Map- Forest")

else: 
         print("Error")

