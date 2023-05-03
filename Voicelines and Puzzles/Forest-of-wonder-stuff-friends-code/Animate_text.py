from yachalk import chalk
import json
import time

def animateText(text):
    storyColour=chalk.bg_rgb(16,19,26).yellow
    for char in text:
        print(storyColour(char), end='', flush=True)
        if char == '.':
          time.sleep(1)
        else:
          time.sleep(0.075)

animateText('some text here...')