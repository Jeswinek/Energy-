import time
import datetime
import math
import Adafruit_ADS1x15
adc=Adafruit_ADS1x15.ADS1115()
GAIN=1
while True:
 v2=0
 vsquare=0
 for i in range(100):
   x=adc.read_adc(0,gain=GAIN)-512
#   v=(-0.0000000001278*x*x*x*x*x+0.000000035029*x*x*x*x+0.00001023*x*x*x-0.003271*x*x+2.853*x-5.57)
#   v=(-0.00000004888*x*x*x*x+0.00002986*x*x*x-0.005183*x*x+2.922*x-6.085)
#   v=(0.0007711*x*x+2.506*x+0.2662)
#   v=(2.709*x-8.35) 
   v=((0.00000412*x*x*x)-(0.000857*x*x+2.675*5)-3.198)
   v2=v*v
   vsquare=vsquare+v2
   time.sleep(0.001)
 vrms=math.sqrt(vsquare/100)
 print (vrms)
 print (x)
 time.sleep(2)
