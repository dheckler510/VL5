import board
from adafruit_motor import stepper
from adafruit_motorkit import MotorKit

kit = MotorKit(i2c=board.I2C())

for i in range(350):
        kit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
        
kit.stepper1.release()

for i in range(400):
        kit.stepper2.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
        
kit.stepper2.release()
