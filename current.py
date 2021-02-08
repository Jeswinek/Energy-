import time
import Adafruit_ADS1x15
import math
import wiringpi,time

adc = Adafruit_ADS1x15.ADS1115()
GAIN = 1
values = [0]*100
while True:
 for i in range(100):
  values[i] = adc.read_adc(0, gain=GAIN)
 print(max(values))
