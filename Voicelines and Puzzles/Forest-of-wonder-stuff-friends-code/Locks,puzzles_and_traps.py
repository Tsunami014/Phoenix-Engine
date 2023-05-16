#Locks,Puzzles and traps are stored in this file so they are easy to read and edit.
import random
import time
import json


#Swap Lock can be modified to Work with Viggo's Music Lock
#Diffrent Colours Must be lined together. To work 
colour_options={"red","yellow","blue","green"}
empty_slots={"Empty,Empty"}
print(colour_options)
#Make the colour options assinable to a number or a slot
slot_1=random.choice(colour_options+empty_slots)
colour_options.remove(slot_1)
slot_2=random.choice(colour_options+empty_slots)
colour_options.remove(slot_2)
slot_3=random.choice(colour_options+empty_slots)
colour_options.remove(slot_3)
slot_4=random.choice(colour_options+empty_slots)
slot_5=random.choice(colour_options+empty_slots)






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


#The Mirror Puzzle is one of the Puzzles. The room contains a large mirror on one wall with hieroglyphs etched into its surface. Across the room, there is another wall with a series of hieroglyphs. The players must reflect a beam of light from a source (e.g., a crystal or a torch) onto a specific hieroglyph on the opposite wall.

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

#PUZZLE 3

#The players enter a dark chamber with a large stone scale in the center. The scale has two plates, each with different hieroglyphs engraved on them. The players notice that the scale is unbalanced, with one plate tilted downwards.
#The players examine the hieroglyphs on the plates and see that each symbol has a numerical value. They also notice that the scale has markings on each side, indicating the weight needed to balance it.

#The players must quickly calculate which combination of hieroglyphs will balance the scale and place them on the plates. If they choose the wrong combination, the scale will tip, and snakes will fall...

#Once the players correctly balance the scale, the snakes retreat back into the ceiling, and a door opens, leading to the next chamber.

#End of Puzzles for Ancient Egypt