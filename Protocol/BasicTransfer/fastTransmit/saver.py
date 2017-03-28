#working for ~520KB jpeg @ ~64KBps

import serial
from time import sleep
port = 'COM3'
ser = serial.Serial(port, 500000)
ser.timeout = 20
sleep(1)
print ("ready")
ser.reset_input_buffer()
sleep(1)
xyz = ser.read(2000000)
print(xyz.decode("latin-1"))
with open("pic.jpg","wb") as w:
     w.write(xyz[2:])
w.close() 
