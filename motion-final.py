import time

from gpiozero import MotionSensor


pir = MotionSensor(4)

while True:
    if pir.motion_detected:
        print('Intruder detected!')
        time.sleep(2)
    else:
        print('No Intruder...')
        time.sleep(2)

