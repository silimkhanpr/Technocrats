import os
from time import sleep
import serial
ser = serial.Serial('COM3', 57600)
sleep(2)
print("initialized")

obj = open("SIHDDP28.pdf", "rb")
data = obj.read()
print(type(data))

fileSize = os.path.getsize("SIHDDP28.pdf")

print ("The size is ", fileSize)

i=0

while (i < fileSize):
    ser.write(data[i:i+8])
    print (data[i:i+8])
    #print ("Output buffer has: ", ser.out_waiting)
    i=i+8

print("done")



