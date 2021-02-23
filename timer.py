from firebase import firebase
import time

firebase= firebase.FirebaseApplication ("https://energy-meter-project-c13ac.firebaseio.com/",None)
j=0
k=0
p=0

def alrm():
   p=0
   while(p<plug):
    p+=1
    time.sleep(1)
   print ("plug is off")
   result = firebase.put('/plugTimer','status',"off")
#   GPIO.output(32,GPIO.HIGH)
   
while True:
  onoff=firebase.get('/plugTimer','status')
  if(onoff=="on"):
    if(j==0):
     plug=firebase.get('/plugTimer','Plug1')
     print ("on")
     print (plug)
     j+=1
     k=0
     alrm()
#     GPIO.output(32,GPIO.LOW)
  if(onoff=="off"):
   if(k==0):
    print ("timer off")
    k+=1
    j==0

