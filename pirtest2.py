while True:

    i=GPIO.input(11)

        if i==0: #When output from motion sensor is LOW

            print ("No intruders",i)

            GPIO.output(3, 0) #Turn OFF LED

            time.sleep(0.1)

        elif i==1: #When output from motion sensor is HIGH

            print ("Intruder detected",i)

            GPIO.output(3, 1) #Turn ON LED

            time.sleep(0.1)
