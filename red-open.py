from adafruit_motorkit import MotorKit

import board
from adafruit_motor import stepper
from adafruit_motorkit import MotorKit

# Initialise the first hat on the default address
kit1 = MotorKit()
# Initialise the second hat on a different address
kit2 = MotorKit(address=0x61)


for i in range(380):
        kit2.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
        
kit2.stepper1.release()

for i in range(400):
        kit1.stepper2.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
        
kit1.stepper1.release()
