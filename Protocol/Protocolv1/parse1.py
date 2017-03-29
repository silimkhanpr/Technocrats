import serial 
import binascii
from time import sleep
ser=serial.Serial('/dev/ttyACM0',500000)
sleep(2)
print('ready')

def parsing(bytes):
	b = bytearray(a)
	UID = b[10:13]
	size = b[15:21]
	data = b[23:23+int(size)]
	crc = b[25+int(size):36+int(size)]
	crc_chck = hex(binascii.crc32(data))
	if (crc_chck == int(crc)):
		f = open("Receive.txt", "ab")
		f.write(data)
		serial.write("OK".encode())
	else:
		serial.write("FAIL".encode())

