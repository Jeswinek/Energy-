import datetime
import RPi.GPIO as GPIO
import multiprocessing
import time
import mysql.connector
from firebase import firebase
#from firebase_admin import db
myconn = mysql.connector.connect(host = "localhost",user = "adminpi",passwd = "#aA12345678",database = "iemcs")
firebase = firebase.FirebaseApplication("https://energy-meter-project-c13ac.firebaseio.com/",None)
sensor = 16

k=0
n=0
data=0
m=0

GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor,GPIO.IN)

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
  #      time.sleep(0.2)
