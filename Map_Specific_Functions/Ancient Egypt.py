import random
import time
sword_in_stone_pullers={"name: Riley","name: Imzafish","name: Max","name: Viggo",}
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
    if ans_riddle_3==("zebra"):
        print("Correct Answer, proceed")
    else:
         print("Wrong Answer")
         #Kill the player
elif riddle_num==4:
    ans_riddle_5=input("The more you take, the more you leave behind. What am I?")
    if ans_riddle_5=="footsteps":
        print("Correct answer, proceed")
    else:
         print("Wrong Answer")
         #Kill the player
else:
    ans_riddle_5=input( "What goes up, but never comes down?")
    if ans_riddle_5==("age"):
         print("Correct answer, proceed")
    else:
         print("Wrong Answer")
        #Kill the player

#funny lock
maze_finished=False
if maze_finished==True:
    print("You have finished the maze")
    time.sleep(1)
    print("A rustic old lock blocks your path")
    print("You attempt to lockpick the lock however you decide to kick it instead")
    kick=input("Press K to continue")
    if kick=="K":
         print("You have successfully kicked the lock")
         print ("The door swings open")

#Defining the Enmies
#Mummies 25hp
#Swarm of Scorpians 45hp
#Snake 50hp

#boss fight
#have to kill two minions and the boss itself
#Pharoh's Guards 50hp each
#Pharoh  100hp



#Sword in Stone 
Can_pull=True
chance_to_pull=random.randint(1,4)
if chance_to_pull==4:
     print("You are the almighty and have pulled the sword in the stone")
     name=input("You shall be recorded what is your name?(Please note your name will be recorded in the game)")
     sword_in_stone_pullers.update ({'name': name})
else:
     print("You have not pulled the sword in the stone")
     print("You cannot attempt to pull the sword in the stone again until you restart the game")
     Can_pull=False
     
#End of Map speficfic functions