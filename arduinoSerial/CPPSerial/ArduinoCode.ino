void setup()
{
  Serial.begin(9600);
}

void loop()
{
  String input;
  input = Serial.readStringUntil('\n');
  Serial.println(input);
  delay(5000);
}
