import serial
from time import sleep
port = 'COM4'
ser = serial.Serial(port,57600)
ser.timeout = 30
sleep(1)
print ("ready")
ser.reset_input_buffer()
sleep(1)
xyz = ser.read(160000)
print(xyz.decode("latin-1"))
with open("shi.pdf","wb") as w:
     w.write(xyz)
w.close() 
