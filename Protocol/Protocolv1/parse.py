import serial 
import binascii
from time import sleep

def parsing(a):
	b = bytearray(a)
	UID = b[8:11]
	size = b[13:19]
	#print size
	data = b[21:21+int(size)]
	crc = b[23+int(size):-8]
	crc = int(str(crc),16)
	crc_chck = hex(binascii.crc32(data))
	crc_chck = int(str(crc_chck),16)
	if (crc_chck == crc):
		#print (data)
		f = open("Receive.txt", "ab")
		f.write(data)
		serial.write("OK".encode())
		f.close()
	else:
		serial.write("FAIL".encode())
	

ser=serial.Serial('/dev/ttyACM0',500000)
sleep(2)
print('ready')
bit = ser.read(5)
parsing(bit)

