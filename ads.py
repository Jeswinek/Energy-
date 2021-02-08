import time

import Adafruit_ADS1x15

adc= Adafruit_ADS1x15.ADS1115()

GAIN=1

adc.start_adc(0, gain=GAIN)

print ("reading")
start = time.time()
while (time.time() - start) <=5.0:
 value = adc.get_last_result()
 print ("channel 0: {0}".format(value))
 time.sleep(0.5)
adc.stop_adc()
