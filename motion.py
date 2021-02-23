from firebase import firebase
import RPi.GPIO as GPIO
import time

firebase= firebase.FirebaseApplication ("https://energy-meter-project-c13ac.firebaseio.com/",None)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.IN)
GPIO.setup(18,GPIO.IN)
c=0
j=0
k=0
while True:
 motion=GPIO.input(7)
 motion2=GPIO.input(18)
 if(GPIO.input(7)==0):
  k=1
  print ("k")
  print (k)
  while k==1:
   if(GPIO.input(18)==0):
    c=c+1
    print ("enter")
    print (c)
    k=k+1
    j-=1
    time.sleep(1)
  print ("checking")
  time.sleep(0.1)
 if(GPIO.input(18)==0):
   j=1
   print ("j")
   print (j)
   while j==1:
    if(GPIO.input(7)==0):
     c=c-1
     print ("exit")
     print (c)
     j+=1
     k-=1
     time.sleep(1)
