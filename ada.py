import time
import Adafruit_ADS1x15
import math
adc=Adafruit_ADS1x15.ADS1115()
GAIN=2/3
#print ("reading")
#print ("| {0:>6} | {1:>6} | {2:>6} | {3:>6} |".format(*range(4)))
#print ("-"*37)
#values=0
values=[0]*400
while True:
 #value=[0]*4
 for i in range(400):
 # values[i]=0
  values[i]=adc.read_adc(0,gain=GAIN)
 # time.sleep(0.1)
 # values=value[i]
  #valu=values-4000
 #print ("| {0:>6} |".format(valu))
 print (max(values))
 value = (max(values)-12800)
 valu = value-24112
 print (value)
 amps= value
# print (value)
# time.sleep(0.001)

