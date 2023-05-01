#Locks,Puzzles and traps are stored in this file so they are easy to read and edit.
#Boring Digital Lock
# Define the file to store the combination
import random
filename = "combination.txt"
from yachalk import chalk
import time

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
# Read the initial combination from the file
with open(filename, "r") as file:
    combination = file.read().strip()

# Ask user if they want to change the combination
animateText(testwrite[4])
change = input()

# If user wants to change the combination, ask for the original and new combinations
if change == "y":
    animateText(testwrite[5])
    old_combination = input()
    if old_combination == combination:
        animateText (testwrite[6])
        new_combination = input()
        with open(filename, "w") as file:
            file.write(new_combination)
        combination = new_combination
        print("Combination changed.")
    else:
        print("Incorrect combination. Cannot change password.")

# Ask user for the combination
user_input = input("Enter the combination: ")

# Check if the combination is correct
if user_input == combination:
  print("Access granted!")
else:
  print("Access denied.")




#Swap Lock can be modified to Work with Viggo's Music Lock
#Diffrent Colours Must be lined together. To work 






#This is code to order a set of Orbs or an Orb lock
# Don't forget this I have it above but will be needed normally; import random 
orb_lock_solved=False
number_clue=random.randint(1,3)
codeinput=["Red","yellow","blue","green"]
orbcode_options=["Red","yellow","blue","green"]
orbcode=random.shuffle(orbcode_options)
print(orbcode_options)
cluepart1=["In the center of the room stands an ornate fountain filled with water and four floating orbs - red, blue, yellow and green - each emitting its own unique light. Above them hangs a sign written in ancient runes which reads 'Order these Orbs'","A book shelf appears with multiple books but four catch your eye namely 'Blue Seas' by ; Joanna A, 'Murder Mysteries' by Callum Green, 'Red is the colour of Love' by Brigette L  and  'Postivity' by Peter Yellow","YA"]
if number_clue==1:
  orb1set_clue=cluepart1[0]
  print(orb1set_clue)
elif number_clue==2:
  orb2set_clue=cluepart1[1]
  print(orb2set_clue)
else:
  orb_last_set_clue=cluepart1[-1]
  print(orb_last_set_clue)
cluepart2=["What do you bury when it's alive and dig up when it's dead?","What's bought by the Yard but worn by the foot?"]


Solution_orb_text=["The Books rustle jumping around only for the books to splinter in a shower of paper, showing their true form as Orbs with four being coloured and the rest a mystical white." "The Orbs spin circling in a "]
#End of Basic Locks which can be slightly modified to fit most other Locks

#Arcade lock 
# A lock where you have to select the correct arcade game to solve it.
game_played = input("There are multiple different arcade machines here... Tetris, Space Invaders, Portal and Pacman. Which do you play? > ")
el_solved = False
if game_played in ["Space Invaders", "space invaders", "Space invaders", "space Invaders"]:
  print("You play Space Invaders and hit the final level... The blood rushes to your head, your arms go tingly, and you drink a convenient bottle of GFuel muck! Then you beat the level. To be honest it was pretty easy.")
  print("You hear a blipping sound and fanfare comes from the arcade machine which now displays: You have beaten Space Invaders!")
  print("Maybe you should check the cafeteria...")
  el_solved = True
elif game_played in ["Tetris", "tetris", "Portal", "portal", "Pacman", "pacman", "pac man", "Pac Man", "Pac man", "pac Man"]:
  print("You play " + game_played + ", and, somehow, you beat it! Nothing happened. What a waste of time.")
else:
  print("That's NOT A GAME (at least not here)")

#End of eLock
#end of locks
#PUZZLE 1
# How the door puzzle works
#The room is a square with four doors, one on each wall, and each door is marked with a symbol. The walls are decorated with hieroglyphs, and a small pedestal sits in the center of the room with a single object on top. The object is a golden scarab beetle with a series of symbols carved into its back.

#Your task is to decipher the symbols on the scarab beetle and use that information to figure out which door to take in order to escape the room.

#Clues:

#The hieroglyphs on the walls depict a series of symbols that are similar to those on the scarab beetle.
#Each door is marked with a different symbol, but only one of them leads to the exit.
#The symbols on the scarab beetle are arranged in a circular pattern, with one symbol at the center and six others arranged around it.
#To solve the puzzle, you must do the following:

#Decipher the symbols on the scarab beetle by matching them to the hieroglyphs on the walls.
#Arrange the symbols in the correct order by starting with the central symbol and following the circular pattern.
#Use the resulting sequence of symbols to figure out which door to take by matching them to the symbols on the doors.
#For example, if the symbols on the scarab beetle are:

#[Central symbol] - [Symbol A] - [Symbol B] - [Symbol C] - [Symbol D] - [Symbol E] - [Symbol F]

#And the symbols on the doors are:

#Door 1: Symbol C
#Door 2: Symbol E
#Door 3: Symbol F
#Door 4: Symbol B
#Then you would take Door 4, since Symbol B is the second symbol in the sequence on the scarab beetle.



#PUZZLE 2
#The Obelisk Puzzle is a challenging puzzle game that requires players to navigate a room filled with pillars and scorpions. The goal is to arrange the pillars in the correct order to progress to the next level, while avoiding the scorpions and staying alive.

#To begin, the player must first observe the pillars and try to determine the correct order in which they should be arranged. Each pillar may have a symbol or a series of symbols engraved on it, which can provide clues as to their correct sequence. For example, the symbols could be letters or numbers arranged in a specific pattern.

#Once the player has figured out the correct order, they must then approach each pillar and move it into place. However, each pillar is guarded by a group of scorpions that will attack the player if they get too close. The player must use their wits to outmaneuver the scorpions and move the pillars into the correct position.

#As the player progresses through the levels, the puzzles become increasingly difficult, with more pillars to arrange and more scorpions to avoid. The player must use their problem-solving skills and strategic thinking to succeed.

#Overall, the Obelisk Puzzle is a fun and challenging game that requires both mental and physical agility. It is a great way to test your problem-solving abilities and improve your strategic thinking skills.




#Step 1: Observe the Pillars
#Start by observing the pillars in the room and try to identify any patterns or symbols on them. Take note of the number of pillars and their locations in the room.

#Step 2: Identify the Correct Order
#Based on the symbols or patterns on the pillars, try to determine the correct order in which they should be arranged. Look for any clues or hints in the room that may help you identify the correct sequence.

#Step 3: Move the Pillars
#Approach each pillar and move it into place. Be careful not to get too close to the scorpions guarding the pillars, as they will attack if you get too close.

#Step 4: Check Your Progress
#As you move each pillar into place, check your progress to see if you are getting closer to the correct sequence. If you realize that you have made a mistake, don't panic. Simply backtrack and try again.

#Step 5: Navigate the Room
#As you move the pillars, you will need to navigate the room and avoid the scorpions. Be strategic and use your movement to outmaneuver the scorpions and reach the next pillar.

#Step 6: Complete the Puzzle
#Once all the pillars are in the correct order, the puzzle will be complete and you can progress to the next level.

#Tips:

#Take your time and don't rush. It's better to move slowly and carefully than to make a mistake and have to start over.
#Use your movement to your advantage. Try to lure the scorpions away from the pillars you need to move, so that you can approach them safely.
#Keep an eye out for any clues or hints in the room that may help you identify the correct sequence.
#If you get stuck, don't be afraid to backtrack and try again. It may take a few tries to figure out the correct sequence, but with patience and perseverance, you can solve the puzzle.
#End of Obilisk puzzle


#PUZZLE 3


#The Mirror Puzzle is one of the more complex challenges in the Puzzle Room. The room contains a large mirror on one wall with hieroglyphs etched into its surface. Across the room, there is another wall with a series of hieroglyphs. The players must reflect a beam of light from a source (e.g., a crystal or a torch) onto a specific hieroglyph on the opposite wall.

#To do this, the players must use a series of levers and switches to manipulate the mirror and direct the beam of light towards the correct hieroglyph. Each lever or switch corresponds to a different angle or direction that the mirror can be adjusted, and the players must experiment with different combinations to find the correct angle to reflect the beam.

#However, if the players reflect the beam onto the wrong hieroglyph, a trap will be triggered, releasing poisonous gas into the room. The gas will quickly fill the room, making it difficult for the players to breathe and putting them in danger.

#To make the puzzle more challenging, the hieroglyphs on the opposite wall may be written in code or require a specific order to be solved. The players must decipher the clues and use their problem-solving skills to solve the Mirror Puzzle and move on to the next challenge



#To solve the Mirror Puzzle, the players need to follow these steps:

#Identify the hieroglyph that needs to be illuminated: The players must carefully study the wall with the hieroglyphs and determine which one needs to be illuminated. This could be indicated by a clue or a symbol in the room.

#Find the light source: The players need to locate the source of the beam of light. It could be a crystal, a torch, or some other object in the room.

#Adjust the levers and switches: The players must use the levers and switches to manipulate the mirror and direct the beam of light towards the correct hieroglyph. They can experiment with different combinations until they find the right angle to reflect the beam.

#Check the hieroglyph: Once the players believe they have reflected the beam of light onto the correct hieroglyph, they need to check it. They can do this by looking at the hieroglyph and verifying that it has been illuminated.

#Move on to the next challenge: If the correct hieroglyph has been illuminated, the players can move on to the next challenge. If not, they need to continue adjusting the mirror until they get it right.

#It's essential to be careful and deliberate when solving the Mirror Puzzle, as reflecting the beam of light onto the wrong hieroglyph will trigger the trap, releasing poisonous gas into the room.

#PUZZLE 4

#The players enter a dark chamber with a large stone scale in the center. The scale has two plates, each with different hieroglyphs engraved on them. The players notice that the scale is unbalanced, with one plate tilted downwards.
#The players examine the hieroglyphs on the plates and see that each symbol has a numerical value. They also notice that the scale has markings on each side, indicating the weight needed to balance it.

#The players must quickly calculate which combination of hieroglyphs will balance the scale and place them on the plates. If they choose the wrong combination, the scale will tip, and snakes will fall...

#Once the players correctly balance the scale, the snakes retreat back into the ceiling, and a door opens, leading to the next chamber.




#The Smell Lock
  #If the player has an Incense Stick in their inventory, the player can set it on fire with an oven to unlock the smell lock

#End of Codes