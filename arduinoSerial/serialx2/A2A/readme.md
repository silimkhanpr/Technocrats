http://www.sdrobots.com/tech-thurday-005-arduino-arduino-serial-communication/
https://github.com/SuperDroidRobots/Arduino-to-Arduino-Serial

The sender packetizes the data with a sync byte, payload, and checksum. The reciever watches for the sync byte, reads in the data, and validates the checksum.
