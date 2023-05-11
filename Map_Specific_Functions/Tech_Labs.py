import random
import time
from yachalk import chalk
import json

def glitchText(text):
    storyColour=chalk.bg_rgb(16,19,26).red_bright
    for char in text:
        print(storyColour(char), end='', flush=True)
        if char == '.':
          time.sleep(random.randint[1,1.5,2])
        else:
          time.sleep(random.randint[0,0.5,1,1.5,2,2.5,3])

with open("glitchtext.md", "r") as f:
  gameText = f.read()
  glitch = gameText.split('\n\n')

print()
glitchText(glitch[0])