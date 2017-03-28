#works for ~290KB jpeg. Extra write start leak NULL bytes
#working 4Mbit rate. for ~279KB

import os
from time import sleep
import serial
ser = serial.Serial('COM4', 500000)
sleep(2)
print("initialized")

obj = open("pic.jpg", "rb")
data = obj.read()
print(type(data))

fileSize = os.path.getsize("pic.jpg")

print ("The size is ", fileSize)
ser.reset_output_buffer()
i=0


while (i < fileSize):
    ser.write(data[i:i+1024])
    sleep(0.000001)
    #print (data[i:i+1000])
    #print ("Output buffer has: ", ser.out_waiting)
    i=i+1024

print("done")



