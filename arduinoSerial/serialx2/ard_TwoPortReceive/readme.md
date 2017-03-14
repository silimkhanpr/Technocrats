## Two Port Receive

from: https://www.arduino.cc/en/Tutorial/TwoPortReceive

Arduino and Genuino boards have built in support for serial communication on pins 0 and 1,
but what if you need more serial ports?

The [SoftwareSerial](https://www.arduino.cc/en/Reference/SoftwareSerial) Library has been developed to allow serial communication to take place
on the other digital pins of your boards, using software to replicate the functionality of 
the hardwired RX and TX lines. This can be extremely helpful when the need arises to communicate 
with two serial enabled devices, or to talk with just one device while leaving the main serial port open for debugging purpose.

In the example below, digital pins 2 and 4 on your Arduino or Genuino board are used as virtual 
RX serial lines. Pins 3 and 5 are virtual TX lines. The board listens on one virtual port (portOne) 
until it receives a "?" character. After that, it listens on the second virtual port (portTwo).
