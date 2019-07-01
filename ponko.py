# Ponko by Naoned Makers
# Now let's play guitar!
# Juin 2019

# LIBS

import RPi.GPIO as GPIO
from adafruit_servokit import ServoKit
import time
import random
import pygame
from glob import glob

# ACTIONS
def Head_Slowly(sleep = 0.02):
  for i in range(90):
    kit.servo[1].angle = 90 - i
    time.sleep(sleep)
  for i in range(180):
    kit.servo[1].angle = i
    time.sleep(sleep)
  for i in range(90):
    kit.servo[1].angle = 180 - i
    time.sleep(sleep)

# Sounds

filenames = glob('sounds/*.ogg') # Where are sounds to play!
pygame.init()
#pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.mixer.init()


def Play_Random_Sound(): # Play random sound from the .OGG files in the directory
  pygame.mixer.stop()
  pygame.mixer.init()
  pygame.mixer.Sound(random.choice(filenames)).play()

"""
files = os.listdir(soundpath)
for name in files:
    print(name)
"""
"""
def Play_Sound_1():
  pygame.mixer.stop()
  pygame.mixer.init()
  pygame.mixer.Sound("sounds/sound12.ogg").play()
  
def Play_Sound_2():
  pygame.mixer.stop()
  pygame.mixer.init()
  pygame.mixer.Sound("sound_2.ogg").play()

def Play_Sound_3():
  pygame.mixer.stop()
  pygame.mixer.init()
  pygame.mixer.Sound("sound_3.ogg").play()

def Play_Sound_4():
  pygame.mixer.stop()
  pygame.mixer.init()
  pygame.mixer.Sound("sound_4.ogg").play()

def Play_Sound_5():
  pygame.mixer.stop()
  pygame.mixer.init()
  pygame.mixer.Sound("sound_5.ogg").play()
"""

def button_callback_1(channel):
  print("Button 1 appuyé !")
  #Play_Sound_1()
  #Head_Slowly()
  Play_Random_Sound()
  
def button_callback_2(channel):
  print("Button 2 appuyé !")
  #Play_Sound_2()
  #Head_Slowly()
  Play_Random_Sound()
  
def button_callback_3(channel):
  print("Button 3 appuyé !")
  #Play_Sound_3()
  #Head_Slowly()
  Play_Random_Sound()
  
def button_callback_4(channel):
  print("Button 4 appuyé !")
  #Play_Sound_4()
  #Head_Slowly()
  Play_Random_Sound()
  
def button_callback_5(channel):
  print("Button 5 appuyé !")
  #Play_Sound_5()
  #Head_Slowly()
  Play_Random_Sound()
  
# CONFIGURATION SERVO HAT

kit = ServoKit(channels=8)
  
# CONFIGURATION BUTTONS & GPIO

GPIO.setwarnings(False) # Ignore warning for now
#GPIO.setmode(GPIO.BOARD) # Warning! Use physical pin numbering
GPIO.setmode(GPIO.BCM) # Use GPIO pin numbering

# Button 1 - WHITE wire

#BUTTON_1 = 11 # N°11 = GPIO17
BUTTON_1 = 17 # GPIO17 = N°11

GPIO.setup(BUTTON_1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin to be an input pin and set initial value to be pulled low (off)
GPIO.add_event_detect(BUTTON_1, GPIO.RISING, callback=button_callback_1, bouncetime=10000) # Setup event

# Button_2 - YELLOW wire

BUTTON_2 = 27 # GPIO27 = N°13
GPIO.setup(BUTTON_2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin to be an input pin and set initial value to be pulled low (off)
GPIO.add_event_detect(BUTTON_2, GPIO.RISING, callback=button_callback_2, bouncetime=10000) # Setup event

# Button_3 - BLUE wire

BUTTON_3 = 22 # GPIO22 = N°15
GPIO.setup(BUTTON_3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin to be an input pin and set initial value to be pulled low (off)
GPIO.add_event_detect(BUTTON_3, GPIO.RISING, callback=button_callback_3, bouncetime=10000) # Setup event

# Button_4 - PURPLE wire

BUTTON_4 = 25 # GPIO25 = N°22
GPIO.setup(BUTTON_4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin to be an input pin and set initial value to be pulled low (off)
GPIO.add_event_detect(BUTTON_4, GPIO.RISING, callback=button_callback_4, bouncetime=10000) # Setup event

# Button_5 - GREY wire

BUTTON_5 = 6 # GPIO19 = N°31
GPIO.setup(BUTTON_5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin to be an input pin and set initial value to be pulled low (off)
GPIO.add_event_detect(BUTTON_5, GPIO.RISING, callback=button_callback_5, bouncetime=10000) # Setup event

# OTHERS

message = input("Press enter to quit\n\n") # Run until someone presses enter

GPIO.cleanup() # Clean up
