from adafruit_motorkit import MotorKit

import board
from adafruit_motor import stepper
from adafruit_motorkit import MotorKit

# Initialise the first hat on the default address
kit1 = MotorKit()
# Initialise the second hat on a different address
kit2 = MotorKit(address=0x61)


for i in range(360):
        kit2.stepper2.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
        
kit2.stepper2.release()
