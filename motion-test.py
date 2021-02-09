from gpiozero import MotionSensor
import time

#GPIO.setmode(GPIO.BOARD)
#GPIO.setwarnings(False)
#GPIO.setup(17, GPIO.IN)
#GPIO.setup(3, GPIO.OUT)

pir = MotionSensor(4)

while True:
    pir.wait_for_motion()

    localtime = time.asctime( time.localtime(time.time()) )
    """
    if i==0: #When output from motion sensor is LOW

        print ("No intruders",i, localtime)

        GPIO.output(3, 0) #Turn OFF LED

        time.sleep(0.1)

    elif i==1: #When output from motion sensor is HIGH
    """
    print ("Intruder detected", localtime)
    """
    GPIO.output(3, 1) #Turn ON LED
    """    
    time.sleep(1.5)