#include <dht.h>

#define DHT11_PIN 7
#define AMB_LIGHT_PIN 0

dht DHT;
char dataString[50] = {0};
int ambient_light;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600); // Starting serial communication
}

void loop() {
  // put your main code here, to run repeatedly:
  int chk = DHT.read11(DHT11_PIN);
  ambient_light = analogRead(AMB_LIGHT_PIN);
  Serial.print("temperature ");
  Serial.println(DHT.temperature);
  Serial.print("humidity ");
  Serial.println(DHT.humidity);
  Serial.print("amblight ");
  Serial.println(ambient_light);
  delay(6000);
}
