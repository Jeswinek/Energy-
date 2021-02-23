import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.IN)

pir = GPIO.input(8)

while True:
 if (pir == 1):
  print (pir)
 if (pir==0):
  print (pir) 
 time.sleep(1)
