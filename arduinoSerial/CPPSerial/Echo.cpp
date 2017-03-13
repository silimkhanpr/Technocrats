#include "stdafx.h"
#include<iostream>
#include "SerialClass.h" 
#include <string>
using namespace std;
// application reads from the specified serial port and reports the collected data
char output[256];

/*Portname must contain these backslashes, and remember to
replace the following com port*/


//String for incoming data
char incomingData[256];
int _tmain(int argc, _TCHAR* argv[])
{
	  Serial arduino("\\\\.\\COM12");
  if (arduino.IsConnected()) cout << "Connection Established" << endl;
  else cout << "ERROR, check port name";

  while (arduino.IsConnected()){
    cout << "Write something: \n";
    std::string input_string;
    //Getting input
    getline(cin, input_string);
    //Creating a c string
    char *c_string = new char[input_string.size() + 1];
    //copying the std::string to c string
    std::copy(input_string.begin(), input_string.end(), c_string);
    //Adding the delimiter
    c_string[input_string.size()] = '\n';
    //Writing string to arduino
    arduino.WriteData(c_string, 256);
    //Getting reply from arduino
    arduino.ReadData(output, 256);
    //printing the output
    puts(output);
    //freeing c_string memory
    delete[] c_string;
  }

 return 0;
}
