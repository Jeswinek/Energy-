import datetime
import time
import Adafruit_ADS1x15
import math
adc = Adafruit_ADS1x15.ADS1115()
GAIN =1
voltageLastSample=0
voltageSampleRead=0
voltageSampleSum=0
voltageSampleCount=0
voltageMean=0
RMSvoltageMean=0
while True:
# now=datetime.datetime.now().microsecond
# if (now>=voltageLastSample+1000):
 for i in range(100):
  voltageSampleRead=(adc.read_adc(0,gain=GAIN))-512-19000
 

#  time.sleep(0.001)
  voltageSampleSum=voltageSampleSum+(voltageSampleRead)
 # print (now)
#  print (voltageSampleRead)
#  print ("xxx",voltageSampleSum)
  voltageSampleCount+=1
#  voltageLastSample=now
#  print (voltageSampleCount)
 # print (voltageSampleRead)
 
 
 if (voltageSampleCount>=100):
  
  voltageMean=voltageSampleSum/voltageSampleCount
  RMSvoltageMean=(voltageMean)*1.5
  print ("RMSvoltageMean")
  print (RMSvoltageMean)
  print ("xxxx",voltageMean)
  voltageSampleSum=0
  voltageSampleCount=0
  time.sleep(2)
