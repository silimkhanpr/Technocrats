import serial
from time import sleep
port = 'COM4'
ser = serial.Serial(port,57600)



def listener(*args):
    print ("waiting")
    ser.timeout = 3
    ser.reset_input_buffer()
    serIn = ser.read(8)
    str = serIn.decode()
    if "SAVE" in str:
        print("RECEIVER_MODE = True")
        ser.write("READY TO RECEIVE".encode())
        sleep(0.1)
        saver(1)
    else:
        print("RESETTING")
        return()
        

    
def saver(*args):
    ser.timeout = 5

    xyz = ser.read(6)

    print(xyz.decode("latin-1"))
    with open("datar.txt","wb") as w:
        w.write(xyz)
    w.close()
    reply = "data was" + xyz.decode()

    ser.write(reply.encode())
    return()

print ("in main")
sleep(2)
while True:
    #print("in while main")
    listener(1)
    
