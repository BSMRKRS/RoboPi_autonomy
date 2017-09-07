import RoboPiLib as RPL
RPL.RoboPiInit("/dev/ttyAMA0",115200)

# Variable Assignment
motor_r = 0
motor_l = 1

motor_r_forward = 2500
motor_r_back = 500
motor_l_forward = 2500
motor_l_back = 500

# Continuous Loop
while True:
  RPL.servoWrite(motor_r, motor_r_forward)
  RPL.servoWrite(motor_l, motor_l_forward)
