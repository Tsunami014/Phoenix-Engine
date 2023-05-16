import random
import time
#voicelines
#work in progress
def Voicelines():
  print('Vaules')
#Swap lock

#Pushing Boulder


#Character Choosing
character_choice=input("Choose a character")

#NPC Dialogue
if character_choice=="hi":
     print("filler")

#Quicksand
#The player needs to press the button and then do a quick reaction test to confirm they made it across.
if button_pressed==True:
     print("Get ready")
     time.sleep(1)
    
#Spinx code
print("Welcome Mortal solve this riddle to continue or DIE")
riddle_num=random.int(1,5)
if riddle_num==1:
     ans_riddle_1=input("Tutenkhamun's mother has 4 sons, North, East, West and one other, who is the fourth")
     if ans_riddle_1=="Tutenkhamun":
                print("Correct Answer, proceed")
     else :
          print("Wrong Answer")
          #Kill the player
elif riddle_num==2:
    ans_riddle_2=input("What can run but cannot walk")
    if ans_riddle_2.lower() =="river":
        print("Correct Answer, proceed")
    else:
        print("Wrong Answer")
        #Kill the player
elif riddle_num==3:
    ans_riddle_3=input("What goes from Z to A")
    if ans_riddle_3==(""):
        print("error")
elif riddle_num==4:
    print("hi")
else:
    ans_riddle_5=input( "What goes up, but never comes down?")
    if ans_riddle_5==("age"):
         print("Correct answer, proceed")
    else:
         print("Wrong Answer")
        #Kill the player

#The more you take, the more you leave behind. What am I?

#answer Footsteps
 #What goes up, but never comes down?

#A: Age