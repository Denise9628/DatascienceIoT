import RPi.GPIO as GPIO
import time

SENSOR_PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)

def my_callback(channel):
  #App here
  print('Intruder detected')
  
try:
  GPIO.add_event_detect(SENSOR_PIN , GPIO.RISING, callback=my_callback)
  while True:
    time.sleep(100)
except KeyboradInterrupt:
  print('Finish')
GPIO.cleanup()
