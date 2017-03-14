## Software Serial Example

from: https://www.arduino.cc/en/Tutorial/SoftwareSerialExample

Arduino and Genuino boards have built in support for serial communication on pins 0 and 1, 
but what if you need more serial ports? 
The SoftwareSerial Library has been developed to allow serial communication to take place on the 
other digital pins of your boards, using software to replicate the functionality of the hardwired RX and TX lines. 
This can be extremely helpful when the need arises to communicate with two serial enabled devices, or to talk with 
just one device while leaving the main serial port open for debugging purpose.

In the example below, digital pins 10 and 11 on your Arduino or Genuino boards are used as virtual RX and 
TX serial lines. The virtual RX pin is set up to listen for anything coming in on via the main serial line,
and to then echo that data out the virtual TX line. 
Conversely, anything received on the virtual RX is sent out over the hardware TX.

