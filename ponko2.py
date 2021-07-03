#!/usr/bin/python3
# Ponko by Naoned Makers
# naoned-makers.github.io
# Now let's play guitar!
# Juin 2019

# LIBS

import time
import random
import pygame
from glob import glob
import getopt
import sys
from threading import Thread

########################################
### Parameters / Constantes
########################################

ARM_CHANNEL = 2

ARM_POS_MAX_BOTTOM = 100 # Max bottom value
ARM_POS_MAX_TOP = 30 # Max top value

HEAD_CHANNEL = 1 

HEAD_LONG_POS_LEFT = 180 # Max left value
HEAD_LONG_POS_MIDDLE = 90 # Middle value
HEAD_LONG_POS_RIGHT = 0 # Max right value

#HEAD_SHORT_POS_LEFT = 130 # Max left value
#HEAD_SHORT_POS_MIDDLE = 90 # Middle value
#HEAD_SHORT_POS_RIGHT = 50 # Max right value

HEAD_SHORT_POS_LEFT = 130 # Max left value
HEAD_SHORT_POS_MIDDLE = 90 # Middle value
HEAD_SHORT_POS_RIGHT = 50 # Max right value

FILENAMES = glob('sounds/*.ogg') # Where are sounds to play!

########################################
### Classes
########################################

class MotorRun(Thread):

    """This Thread will run a function with args ."""

    def __init__(self, function_name, *args):
        Thread.__init__(self)
        self.function = function_name
        self.args = args

    def run(self):
        """Code à exécuter pendant l'exécution du thread."""
        eval(self.function)(*self.args)

########################################
### Functions
########################################

def arm(kit, pygame, sleep = 0.002):
  print("Moving arm")
  '''
    Make the Arm movement
  '''
  while pygame.mixer.get_busy() > 0:
    for i in range(ARM_POS_MAX_BOTTOM - ARM_POS_MAX_TOP):
      kit.servo[ARM_CHANNEL].angle = ARM_POS_MAX_BOTTOM - i
      time.sleep(sleep)
    for i in range(ARM_POS_MAX_BOTTOM - ARM_POS_MAX_TOP):
      kit.servo[ARM_CHANNEL].angle = ARM_POS_MAX_TOP + i
      time.sleep(sleep)

def head_long(kit, pygame, sleep = 0.005):
  print("Moving head_long")
  '''
    Make the Head long movement
  '''
  while pygame.mixer.get_busy() > 0:
    for i in range(HEAD_LONG_POS_MIDDLE - HEAD_LONG_POS_RIGHT):
      kit.servo[HEAD_CHANNEL].angle = HEAD_LONG_POS_MIDDLE - i
      time.sleep(sleep)
    for i in range(HEAD_LONG_POS_LEFT - HEAD_LONG_POS_RIGHT):
      kit.servo[HEAD_CHANNEL].angle = HEAD_LONG_POS_RIGHT + i
      time.sleep(sleep)
    for i in range(HEAD_LONG_POS_LEFT - HEAD_LONG_POS_MIDDLE):
      kit.servo[1].angle = HEAD_LONG_POS_LEFT - i
      time.sleep(sleep)

def head_short(kit, pygame, sleep = 0.001):
  print("Moving head_short")
  '''
    Make the Head short movement
  '''
  while pygame.mixer.get_busy() > 0:
    for i in range(HEAD_SHORT_POS_MIDDLE - HEAD_SHORT_POS_RIGHT):
      kit.servo[HEAD_CHANNEL].angle = HEAD_SHORT_POS_MIDDLE - i
      time.sleep(sleep)
    for i in range(HEAD_SHORT_POS_LEFT - HEAD_SHORT_POS_RIGHT):
      kit.servo[HEAD_CHANNEL].angle = HEAD_SHORT_POS_RIGHT + i
      time.sleep(sleep)
    for i in range(HEAD_SHORT_POS_LEFT - HEAD_SHORT_POS_MIDDLE):
      kit.servo[HEAD_CHANNEL].angle = HEAD_SHORT_POS_LEFT - i
      time.sleep(sleep)

def play_random_sound(pygame): # Play random sound from the .OGG files in the directory
  pygame.mixer.stop()
  pygame.mixer.init()
  pygame.mixer.Sound(random.choice(FILENAMES)).play()

def Play_GOT(pygame): # Play GOT theme!
  pygame.mixer.stop()
  pygame.mixer.init()
  pygame.mixer.Sound("sounds/GOT.ogg").play()

def button_callback_1(kit,pygame):
  print("Button 1 appuyé !")
  
  play_random_sound(pygame)

  #Thread creation
  thread_1 = MotorRun("head_short",kit,pygame)
  thread_2 = MotorRun("arm",kit,pygame)

  # Launch Threads
  thread_1.start()
  thread_2.start()

  # Wait for thread ending
  thread_1.join()
  thread_2.join()
  
def button_callback_2(kit,pygame):
  print("Button 2 appuyé !")
  play_random_sound(pygame)

  #Thread creation
  thread_1 = MotorRun("head_short",kit,pygame)
  thread_2 = MotorRun("arm",kit,pygame)

  # Launch Threads
  thread_1.start()
  thread_2.start()

  # Wait for thread ending
  thread_1.join()
  thread_2.join()
  
def button_callback_3(kit,pygame):
  print("Button 3 appuyé !")
  play_random_sound(pygame)

  #Thread creation
  thread_1 = MotorRun("head_short",kit,pygame)
  thread_2 = MotorRun("arm",kit,pygame)

  # Launch Threads
  thread_1.start()
  thread_2.start()

  # Wait for thread ending
  thread_1.join()
  thread_2.join()
  
def button_callback_4(kit,pygame):
  print("Button 4 appuyé !")
  play_random_sound(pygame)

  #Thread creation
  thread_1 = MotorRun("head_long",kit,pygame)
  thread_2 = MotorRun("arm",kit,pygame)

  # Launch Threads
  thread_1.start()
  thread_2.start()

  # Wait for thread ending
  thread_1.join()
  thread_2.join()
  
def button_callback_5(kit,pygame):
  print("Button 5 appuyé !")
  #play_random_sound(pygame)
  Play_GOT(pygame)

  #Thread creation
  thread_1 = MotorRun("head_short",kit,pygame)
  thread_2 = MotorRun("arm",kit,pygame)

  # Launch Threads
  thread_1.start()
  thread_2.start()

  # Wait for thread ending
  thread_1.join()
  thread_2.join()

def parse_args(argv):
    
  #Default parameters value
  dev_mode = False

  try:
      opts, args = getopt.getopt(argv,":d",[])
  except getopt.GetoptError:
      print ('ponko.py -d')
      sys.exit(2)

  for opt, arg in opts:
    if opt in ("-d", "--dev"):
      dev_mode = True
   
  return dev_mode

########################################
### Main code
########################################

def main(argv):

  # Args parsing
  dev_mode = parse_args(argv)

  if(dev_mode):
    print("dev mode activated !")
    try:
      import importlib.util
      importlib.util.find_spec('RPi.GPIO')
      import RPi.GPIO as GPIO
    except ImportError:
      """
      import FakeRPi.GPIO as GPIO
      OR
      import FakeRPi.RPiO as RPiO
      """
    
      import FakeRPi.GPIO as GPIO

    from unittest.mock import MagicMock
    kit = MagicMock()
  else:
    from adafruit_servokit import ServoKit

    kit = ServoKit(channels=8)

    import RPi.GPIO as GPIO

  # Sounds
  pygame.init()
  pygame.mixer.init()

  # CONFIGURATION BUTTONS & GPIO

  GPIO.setwarnings(False) # Ignore warning for now
  GPIO.setmode(GPIO.BCM) # Use GPIO pin numbering

  # Button 1 - WHITE wire
  BUTTON_1 = 17 # GPIO17 = N°11
  callback_1 = lambda channel, kit_arg = kit, game_arg = pygame: button_callback_1(kit_arg,game_arg)
  GPIO.setup(BUTTON_1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin to be an input pin and set initial value to be pulled low (off)
  GPIO.add_event_detect(BUTTON_1, GPIO.RISING, callback=callback_1, bouncetime=10000) # Setup event

  # Button_2 - YELLOW wire

  BUTTON_2 = 13 # GPIO13 = N°
  callback_2 = lambda channel, kit_arg = kit, game_arg = pygame: button_callback_2(kit_arg,game_arg)
  GPIO.setup(BUTTON_2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin to be an input pin and set initial value to be pulled low (off)
  GPIO.add_event_detect(BUTTON_2, GPIO.RISING, callback=callback_2, bouncetime=10000) # Setup event

  # Button_3 - BLUE wire
  BUTTON_3 = 22 # GPIO22 = N°15
  callback_3 = lambda channel, kit_arg = kit, game_arg = pygame: button_callback_3(kit_arg,game_arg)
  GPIO.setup(BUTTON_3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin to be an input pin and set initial value to be pulled low (off)
  GPIO.add_event_detect(BUTTON_3, GPIO.RISING, callback=callback_3, bouncetime=10000) # Setup event

  # Button_4 - PURPLE wire
  BUTTON_4 = 25 # GPIO25 = N°22
  callback_4 = lambda channel, kit_arg = kit, game_arg = pygame: button_callback_4(kit_arg,game_arg)
  GPIO.setup(BUTTON_4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin to be an input pin and set initial value to be pulled low (off)
  GPIO.add_event_detect(BUTTON_4, GPIO.RISING, callback=callback_4, bouncetime=10000) # Setup event

  # Button_5 - GREY wire
  BUTTON_5 = 6 # GPIO19 = N°31
  callback_5 = lambda channel, kit_arg = kit, game_arg = pygame: button_callback_5(kit_arg,game_arg)
  GPIO.setup(BUTTON_5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin to be an input pin and set initial value to be pulled low (off)
  GPIO.add_event_detect(BUTTON_5, GPIO.RISING, callback=callback_5, bouncetime=10000) # Setup event

  if(dev_mode):

    while True:
      message = input("Press 1 to 5 and Enter to validate or Just Enter to quit\n\n") # Run until someone presses enter
      if(not message):
        break

      #TODO protect against wrong typing
      callable = "button_callback_"+message
      eval(callable)(kit,pygame)
      
     
  else:
    while True:
#        for line in sys.stdin:
#             if 'Exit' == line.rstrip():
#                    break
        time.sleep(1)
#    message = input("Press Enter to quit\n\n") # Run until someone presses enter

  GPIO.cleanup() # Clean up

if __name__ == "__main__":
    main(sys.argv[1:])
