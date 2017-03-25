import serial
port = 'COM4'
ser = serial.Serial(port,9600)
ser.timeout = 60
xyz = ser.read(160000)
print(xyz.decode("latin-1"))
with open("sih.pdf","wb") as w:
     w.write(xyz)
w.close() 
