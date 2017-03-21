import binascii
import zlib

fil = open('myfile3.txt', 'rb')
oh=fil.read()

bits = zlib.decompress(oh)
#print (bits)
with open('rpi2.pdf', 'wb') as w:
    w.write(bits)
