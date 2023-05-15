import random
import time
#Amour Snapping
#work in progress
def amour_snapping_mechanism(item):
    helmet_slot_filled=False
    amour_slot_filled=False
    charm_slot_filled=False
   
    
    amour_slot=={}
if "#amour" in item.tag:
    amour_slot =item
    amour_slot_filled=True
elif"#helmet" in item.tag:
    helmet_slot =item
    helmet_slot_filled=True
elif "#charm" in item.tag:
     charm_slot =item
     charm_slot_filled=True
else:
     print("No amour or helmet or charm slot found")
     exit()











#Swap lock

#Pushing Boulder


#Character Choosing
character_choice=input("Choose a character")

#NPC Dialogue
if character_choice=="hi":
     print("filler")


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
    if ans_riddle_5==(""):
         print("Correct answer, proceed")
    else:
         print("Wrong Answer")

#The more you take, the more you leave behind. What am I?

#answer Footsteps
 #What goes up, but never comes down?

#A: Age