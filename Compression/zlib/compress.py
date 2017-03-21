import zlib
import binascii

filobject = open('cs.pdf', 'rb')
oh=filobject.read()

bits = zlib.compress(oh, level=9)
#print (bits)
with open('myfile3.txt', 'wb') as w:
    w.write(bits)
