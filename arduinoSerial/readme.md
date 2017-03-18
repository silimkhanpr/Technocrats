# References


https://www.arduino.cc/en/reference/serial



Virtual Serial: Example with redirection:
https://www.arduino.cc/en/Tutorial/SoftwareSerialExample

PySerial:
https://github.com/tino/pyFirmata/blob/master/README.rst

PySerial+Arduino (loopback all ASCII, echo back)
http://www.instructables.com/id/Interface-Python-and-Arduino-with-pySerial/?ALLSTEPS

MaxBaudRate
http://arduino.stackexchange.com/questions/296/how-high-of-a-baud-rate-can-i-go-without-errors

AltSoft serial:
https://www.pjrc.com/teensy/td_libs_AltSoftSerial.html

Pymata:
https://learn.adafruit.com/circuit-playground-firmata/example-python-code

C# Serial:
http://playground.arduino.cc/Csharp/SerialCommsCSharp

-------------
noteToSelf:

#To encode:
serialobject.write(str(chr(integervariable)).encode()) # Convert the decimal number to ASCII then send it to the Arduino

#To decode:
strvar= serialobject.readline()
strvar = strvar.decode()
print(strvar) 

#since:
In Python 3.X, strings such as "abc" by default are Unicode strings. Strings must be encoded for transmission,
or just start with a byte string b"abc" (note the b). Either of these will work:

              serialport.write(b"\x23o0 \x23f")
or:
              serialport.write("\x23o0 \x23f".encode('ascii'))
              
Note that specifying an encoding is optional and defaults to utf8.

Read more@ 
http://stackoverflow.com/questions/34958926/am-having-difficulties-with-unicode-strings-serialport-write-x23o0-x23f-not

Python 2 vs 3: Reading Strings & Bytes from files: 
http://www.pgbovine.net/unicode-python.htm
------------

