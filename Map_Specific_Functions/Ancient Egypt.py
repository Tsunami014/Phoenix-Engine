import random
import time
#Map Selection
input("Please chosse a map")
#Amour Snapping
def amour_snapping_mechanism(item):
    helmet_slot_filled=False
    amour_slot_filled=False
    shoe_slot_filled=True
    charm_slot_filled=False
    shield_slot_filled=False
    
    amour_slot=={}
if "#amour" in item.tag:
    amour_slot =item
elif"#helmet" in item.tag:
    helmet_slot =item
elif "#charm" in item.tag:
     charm_slot =item
     
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

"Choose a map. Type 1 for Ancient Egypt, Type 2 for Tech Labs and Type 3 for Forest. > "

"Loading Map - Ancient Egypt..."

"Loading Map - Tech Labs..."

"Loading Map - Forest..."
def Voicelines():
  print('Vaules')

def Lives():
  Livecount=3
  Death=False
  if Death==True:
    choice=random.randint (1,5)
    if choice==(-1):
      pass










#Swap lock

#Pushing Boulder

#Character Choosing

#NPC Dialogue

#Spinx code
print("Welcome Mortal solve this riddle to continue or DIE")
riddle_num=random.int(1,5)
if riddle_num==1:
     ans_riddle_1=input("Tutenkhamun's mother has 4 sons, North, East, West and one other, who is the fourth")
     if ans_riddle_1=="Tutenkhamun":
                print("Correct Answer, proceed")
elif riddle_num==2:
    ans_riddle_2=input("What can run but cannot walk")
    if ans_riddle_2.lower() =="river":
        print("Correct Answer, proceed")
    else:
        print("Wrong Answer")
elif riddle_num==3:
    ans_riddle_3=input("What goes from Z to A")
    if ans_riddle_3==(""):
        print("error")
elif riddle_num==4:
    print("hi")
else:
    ans_riddle_5=input( "What goes up, but never comes down?")

#The more you take, the more you leave behind. What am I?

#answer Footsteps
 #What goes up, but never comes down?

#A: Age