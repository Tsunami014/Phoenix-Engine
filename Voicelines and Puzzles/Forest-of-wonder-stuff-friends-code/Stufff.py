import json
import random
import time
from yachalk import chalk

def animateText(text):
    storyColour=chalk.bg_rgb(16,19,26).yellow
    for char in text:
        print(storyColour(char), end='', flush=True)
        if char == '.':
          time.sleep(1)
        else:
          time.sleep(0.075)

with open("Cooltext.md", "r") as f:
  gameText = f.read()
  testwrite = gameText.split('\n\n')
 


#It is chosing map
animateText(testwrite[0])
mapchoice=int(input(""))
if mapchoice==1:
    animateText(testwrite[1])
elif mapchoice==2:
    animateText(testwrite[2])
elif mapchoice==3:
    animateText(testwrite[3])

else: 
         print("Error")

def Voicelines():
  print('Vaules')

def Lives():
  Livecount=3
  Death=False
  if Death==True:
    choice=random.randint (1,5)
    if choice==(-1):
      pass