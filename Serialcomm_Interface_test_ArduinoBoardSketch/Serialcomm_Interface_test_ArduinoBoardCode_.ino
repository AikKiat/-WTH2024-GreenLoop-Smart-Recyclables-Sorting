#define LED_BUILTIN 2  // The built-in LED is usually on GPIO 2

void setup() {
  Serial.begin(115200); // Start the serial communication
  pinMode(LED_BUILTIN, OUTPUT); // Set the built-in LED as output
  digitalWrite(LED_BUILTIN, HIGH); // Turn off the LED initially (active LOW)
  Serial.println("ESP32 is ready.");
}

void loop() {
  if (Serial.available() > 0) {
    String incoming = Serial.readStringUntil('\n'); // Read data from the serial port
    incoming.trim(); // Remove any extra whitespace or newline characters

    if (incoming.equalsIgnoreCase("glass")) {
      //digitalWrite(LED_BUILTIN, LOW); // Turn on the LED (active LOW)
      Serial.println("Glass Detected!");
    }

    if (incoming.equalsIgnoreCase("cardboard")) {
      //digitalWrite(LED_BUILTIN, LOW); // Turn on the LED (active LOW)
      Serial.println("cardboard Detected!");
    }

    if (incoming.equalsIgnoreCase("paper")) {
      //digitalWrite(LED_BUILTIN, LOW); // Turn on the LED (active LOW)
      Serial.println("paper Detected!");
    }

    if (incoming.equalsIgnoreCase("metal")) {
      //digitalWrite(LED_BUILTIN, LOW); // Turn on the LED (active LOW)
      Serial.println("metal Detected!");
    }

    if (incoming.equalsIgnoreCase("trash")) {
      //digitalWrite(LED_BUILTIN, LOW); // Turn on the LED (active LOW)
      Serial.println("trash Detected!");
    }
  }
}
