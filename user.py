import datetime
import RPi.GPIO as GPIO
import Adafruit_ADS1x15
import multiprocessing
import time
import math
import serial
import mysql.connector
adc=Adafruit_ADS1x15.ADS1115()
GAIN=1
ser=serial.Serial("/dev/ttyAMA0",9600)
ser.baudrate=9600
values=[0]*100
from firebase import firebase
#from firebase_admin import db
myconn = mysql.connector.connect(host = "localhost",user = "adminpi",passwd = "#aA12345678",database = "iemcs")
firebase = firebase.FirebaseApplication ("https://energy-meter-project-c13ac.firebaseio.com/",None)
sensor = 16

k=0
n=0
data=0
m=0
j=0
t=0
y=0
q=0
p=0

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.IN)
GPIO.setup(sensor,GPIO.IN)
def intruder():
 while True:
  motion=GPIO.input(8)
  if motion==0:
   print ("NO intruders",motion)
   motion= firebase.put('/Automation','Light1_index',"off")
  # time.sleep(0.5)
  elif motion==1:
   print ("intruder dertected",motion)
   motion = firebase.put('/Automation','Light1_index',"on")
  # time.sleep(0.5)
 #GPIO.output(32,GPIO.HIGH)
def alrm():
  p=0
  while(p<plug):
   p+=1
   time.sleep(1)
  print ("plug is off")
  result3 = firebase.put('/plugTimer','status',"off")
  #GPIO.output(32,GPIO.HIGH)

def timm():
 q=0
 y=0
 p=0
 while True:
   onoff=firebase.get('/plugTimer','status')
   if(onoff=="on"):
     if(y==0):
      plug=firebase.get('/plugTimer','Plug1')
      print ("on")
      print (plug)
      y+=1
      q=0
      alrm()
     #GPIO.output(32,GPIO.LOW)
   if(onoff=="off"):
    if(q==0):
     print ("timer off")
     q+=1
     y==0 
def ard():
 while True:
  read_ser=ser.readline().decode('utf-8').rstrip()
  print (read_ser)
  volt = float(read_ser)
  if(volt<234.5):
   print ("under voltage")
def ada():
 j=0
 t=0
 while True:
  for i in range(100):
   values[i]=adc.read_adc(0,gain=GAIN)
  print (max(values))

  if(max(values)>=1):
   if(j==0):
    print ("bulb is on")
    zz="on"
    fb1(zz)
    j+=1
    t=0
  else:
   if(t==0):
    print ("bulb is off")
    zz="off"
    fb1(zz)
    t+=1
    j=0
def fb1(fire1):
# db = firebase.database()
# result = firebase.set('45')
 result1 = firebase.put('',"/Automation/Light1_index",fire1)
 print ("firebase updated")
 print(result1)
def fun():
   return Test()
def fb(fire):
 t = fun()
 kdate = (t.date)
 ktime = (t.time)
 kkey = kdate+ktime
 print(kkey)
 data_unit = {'Unit':fire,'date':kdate,'time':ktime}
# db = firebase.database()
# result = firebase.set('45')
 result = firebase.put('',kkey,fire)
 print ("firebase updated")
 print(result)
class Test:
 def __init__(self):
  now = datetime.datetime.now()
  self.date = now.strftime("%Y%m%d")
  self.time = now.strftime("%M")


def db(data):
 myconn = mysql.connector.connect(host = "localhost", user = "adminpi", passwd = "#aA12345678", database = "iemcs")
 t = fun()
 tdate = (t.date)
 dtime = (t.time)
 cur=myconn.cursor()
 sql="insert into Metre(slno,date,time,unit)""values(%s,%s,%s,%s)"
 val=("1",tdate,dtime,data)
 try:
  cur.execute(sql,val)
  myconn.commit()
 except:
  myconn.rollback()
 print ("record inserted")
 myconn.close()

print ( "IR Sensor Ready....")
print (" ")

def process2():
 
  starttime = time.time()
  while True:
   time.sleep(60.0 - ((time.time() - starttime) % 60.0))
   p = multiprocessing.Process(name='p',target=firebase1) 
   p.start()

def metercount():
 k=0
 n=0
 try:
  while True:
    if GPIO.input(sensor):

      k+=1
      print (k)
      if k>=5:
        n=n+k
        print (n)
        with open("/home/ubuntu/Documents/meter count.txt",'w',encoding = 'utf-8') as f:
          f.write(str (n))
        time.sleep(0.2)
        f = open("/home/ubuntu/Documents/meter count.txt",'r',encoding = 'utf-8')
        data=f.read()
        f.close()
        print (data)
        k=0
        myconn = mysql.connector.connect(host = "localhost",user = "adminpi",passwd = "#aA12345678",database = "iemcs")
        db(data)
       # if int(data)%20==0:
       # p = multiprocessing.Process(name='p',target=firebase1)
       # p.start()
       # data = int(data)+5

      while GPIO.input(sensor):
         time.sleep(0.1)
 except KeyboardInterrupt:
    GPIO.cleanup()

def firebase1():
  k=1
  try:
    while k==1:
      #  with open("/home/ubuntu/Documents/meter count.txt",'r',encoding = 'utf-8') as f:
       #   m = f.read()
      #  z = int(m)
        time.sleep(0.1)
        f = open("/home/ubuntu/Documents/meter count.txt", 'r', encoding = 'utf-8')
        m = f.read()
        f.close()
        z = int(m)
      #  if x>z:
       #  if z%30==0:
        fb(z)
        print ("firebase value:")
        print (z)
        k+=1
 #       p = multiprocessing.Process(name='p',target=firebase1)
 #       p.terminate()

  except KeyboardInterrupt:
     GPIO.cleanup()
 # finally:
  #   time.sleep(180)
#  finally:
#   p.stop() 
 #  except:
 #   firebase1()
if __name__ == '__main__':
 p1 = multiprocessing.Process(name='p1',target=metercount)
 p1.start()
 p3 = multiprocessing.Process(name='p3',target=process2)
 p3.start()
# p4 = multiprocessing.Process(name='p4',target=ada)
# p4.start()
 p5 = multiprocessing.Process(name='p5',target=ard)
 p5.start()
 p6 = multiprocessing.Process(name='p6',target=timm)
 p6.start()
 p7 = multiprocessing.Process(name='p7',target=intruder)
 p7.start()
  #      time.sleep(0.2)
