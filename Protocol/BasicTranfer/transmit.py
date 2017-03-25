import os
from time import sleep
import serial
ser = serial.Serial('COM3', 9600)
sleep(2)
print("initialized")

obj = open("print.pdf", "rb")
data = obj.read()
print(type(data))

fileSize = os.path.getsize("print.pdf")

print ("The size is ", fileSize)

i=0

while (i < fileSize):
    ser.write(data[i:i+200])
    print (data[i:i+200])
    print ("Output buffer has: ", ser.out_waiting)
    i=i+200



