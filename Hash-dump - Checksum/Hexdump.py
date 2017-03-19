import binascii
b = open('Path' , 'rb').read()
print (binascii.hexlify(b))
