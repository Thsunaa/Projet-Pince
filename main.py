import time
import sys
from adafruit_servokit import ServoKit

kit = ServoKit(channels=8)
num1=int(sys.argv[1])
num2=int(sys.argv[2])

print(sys.argv[1])
kit.servo[num1].angle = num2
kit.continuous_servo[1].throttle = 1