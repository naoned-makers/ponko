from adafruit_servokit import ServoKit
import time

# CONFIGURATION SERVO HAT

kit = ServoKit(channels=8)

#arm_top = 10
#arm_middle = 90
#arm_bottom = 150

## ACTIONS
#def Head_Slowly(sleep = 0.01):
  #for i in range(90):
    #kit.servo[1].angle = 90 - i
    #time.sleep(sleep)
  #for i in range(180):
    #kit.servo[1].angle = i
    #time.sleep(sleep)
  #for i in range(90):
    #kit.servo[1].angle = 180 - i
    #time.sleep(sleep)

#def Arm_Short(sleep = 0.01):
  #for i in range(45):
    #kit.servo[2].angle = 45 - i
    #time.sleep(sleep)
  #for i in range(90):
    #kit.servo[2].angle = i
    #time.sleep(sleep)
  #for i in range(45):
    #kit.servo[2].angle = 90 - i
    #time.sleep(sleep)


##Head_Slowly()
##Arm_Short()

#sleep = 0.2

#kit.servo[2].angle = arm_middle
#time.sleep(sleep)
#kit.servo[2].angle = arm_bottom
#time.sleep(sleep)
#kit.servo[2].angle = arm_middle
#time.sleep(sleep)
#kit.servo[2].angle = arm_top
#time.sleep(sleep)
#kit.servo[2].angle = arm_middle

#kit.servo[2].angle = 20
kit.servo[1].angle = 110
