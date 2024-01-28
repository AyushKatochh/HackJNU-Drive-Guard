// Define sensor and actuator pins
const int mq3Pin = A0;    // Analog input pin for MQ-3 sensor
const int relayPin = 7;    // Digital output pin for relay control
const int motorPin = 11;   // Output pin for controlling DC motor
const int ledPin = 13;     // Output pin for LED
const int buzzerPin = 8;   // Output pin for buzzer

// Define threshold for alcohol detection
const int alcoholThreshold = 500;  // Adjust this value based on sensor calibration

void setup() {
  // Initialize relay, motor, LED, and buzzer pins
  pinMode(relayPin, OUTPUT);
  pinMode(motorPin, OUTPUT);
  pinMode(ledPin, OUTPUT);
  pinMode(buzzerPin, OUTPUT);
  
  // Set relay to initial state (motor on)
  digitalWrite(relayPin, HIGH);
}

void loop() {
  // Read analog value from MQ-3 sensor
  int alcoholLevel = analogRead(mq3Pin);
  
  // Check if alcohol level exceeds threshold
  if (alcoholLevel > alcoholThreshold) {
    // Turn off motor and indicate alcohol detected
    digitalWrite(relayPin, LOW);    // Turn off relay (motor)
    digitalWrite(motorPin, LOW);     // Ensure motor is stopped
    digitalWrite(ledPin, HIGH);      // Turn on LED
    digitalWrite(buzzerPin, HIGH);   // Turn on buzzer
    delay(4000);  // Buzzer sound duration (4 seconds)
    digitalWrite(buzzerPin, LOW);    // Turn off buzzer
    digitalWrite(ledPin, LOW);       // Turn off LED
  } else {
    // Alcohol not detected, keep motor running and turn off LED
    digitalWrite(relayPin, HIGH);   // Turn on relay (motor)
    digitalWrite(motorPin, HIGH);    // Start motor
    digitalWrite(ledPin, LOW);       // Turn off LED
  }
  
  delay(100);  // Adjust delay as needed for responsiveness and power consumption
}