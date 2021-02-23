import serial
import time

ser=serial.Serial("/dev/ttyACM0",9600)
ser.baudrate=9600
while True:
 read_ser=ser.readline().decode('utf-8').rstrip()
 print (read_ser)
 volt = float(read_ser)
 if(volt<234.5):
# volt = volt+1.0
  print ("under voltage")
# var = read_ser.split()
# print (var)
  
# var="b' 7.25 \n'"
# kar= (var.split())
# print (kar[1])
 #print (read_ser.split('\'))
 #pieces=read_ser.split("\n")
 #n=pieces[0]
 #print (n)

