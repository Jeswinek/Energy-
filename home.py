from firebase import firebase
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(32,GPIO.OUT)
GPIO.output(32,GPIO.HIGH)
GPIO.setup(36,GPIO.OUT)
GPIO.output(36,GPIO.HIGH)


firebase = firebase.FirebaseApplication("https://energy-meter-project-c13ac.firebaseio.com/",None)
k=0
j=0
a=0
b=0
c=0
d=0
e=0
f=0
g=0
h=0
m=0
n=0
try:
 while True: 
  Fan1 = firebase.get('/Automation','Fan1')
  Fan2 = firebase.get('/Automation','Fan2')
  Fan3 = firebase.get('/Automation','Fan3')
  Light1 = firebase.get('/Automation','Light1')
  Light2 = firebase.get('/Automation','Light2')
  Light3 = firebase.get('/Automation','Light3')
  if(Fan1=="on"):
   if(k==0):
    print ("Fan1 turned on")
    GPIO.output(32,GPIO.LOW)
    k+=1
    j=0
  else:
   if(j==0):
    print ("Fan1 turned off")
    GPIO.output(32,GPIO.HIGH)
    j+=1
    k=0
  if(Fan2=="on"):
   if(a==0):
    print ("Fan2 turned on")
    GPIO.output(36,GPIO.LOW)
    a+=1
    b=0
  else:
   if(b==0):
    print ("Fan2 turned off")
    GPIO.output(36,GPIO.HIGH)
    b+=1
    a=0
  if(Fan3=="on"):
   if(c==0):
    print ("Fan3 turned on")
    c+=1
    d=0
  else:
   if(d==0):
    print ("Fan3 turned off")
    d+=1

    c=0
  if(Light1=="on"):
   if(e==0):
    print ("Light1 turned on")
    e+=1
    f=0
  else:
   if(f==0):
    print ("Light1 turned off")
    f+=1
    e=0
  if(Light2=="on"):
   if(g==0):
    print ("Light2 turned on")
    g+=1
    h=0
  else:
   if(h==0):
    print ("Light2 turned off")
    h+=1
    g=0
  if(Light3=="on"):
   if(m==0):
    print ("Light3 turned on")
    m+=1
    n=0
  else:
   if(n==0):
    print ("Light3 turned off")
    n+=1
    m=0
  time.sleep(0.2)
except KeyboardInterrupt:
#    GPIO.cleanup()
     print ("quit")
