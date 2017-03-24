import serial
port = '/dev/ttyACM1'
ser = serial.Serial(port,9600)
ser.timeout = 40
xyz = ser.read(160000)
print(xyz.decode("latin-1"))
with open("file.pdf","wb") as w:
 w.write(xyz)
w.close() 
