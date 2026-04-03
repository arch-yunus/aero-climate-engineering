/**
 * @file capsule_release.ino
 * @brief Seeding Capsule Release Controller for Aero-Climate Engineering.
 * @author Meta-Engineering Research Lab
 * 
 * Target: Arduino Nano / STM32 / ESP32
 * Description: Controls the servo-actuated release mechanism for cloud seeding 
 * capsules (Silver Iodide or Liquid Propane).
 */

#include <Servo.h>

// Pin Definitions
#define SERVO_PIN 9
#define STATUS_LED 13
#define COMMAND_INPUT_PIN 2 // High signal from Edge AI / Telemetry receiver

// Servo Positions (in degrees)
#define POS_LOCKED 0
#define POS_RELEASED 110

Servo payloadServo;
bool isSeeding = false;

void setup() {
  Serial.begin(115200);
  pinMode(STATUS_LED, OUTPUT);
  pinMode(COMMAND_INPUT_PIN, INPUT_PULLUP);
  
  payloadServo.attach(SERVO_PIN);
  payloadServo.write(POS_LOCKED); // Ensure locked position on startup
  
  Serial.println("[READY] Payload Control: System Armed and Locked.");
  blinkLED(3);
}

void loop() {
  // Check for trigger signal from Edge AI or Radio receiver
  bool trigger = digitalRead(COMMAND_INPUT_PIN) == LOW; // Assuming active low logic
  
  if (trigger && !isSeeding) {
    executeRelease();
  } else if (!trigger && isSeeding) {
    resetPayload();
  }
}

void executeRelease() {
  Serial.println("[ACTION] RELEASE COMMAND DETECTED! Initiating seeding...");
  digitalWrite(STATUS_LED, HIGH);
  payloadServo.write(POS_RELEASED);
  isSeeding = true;
  delay(1000); // Debounce duration
}

void resetPayload() {
  Serial.println("[INFO] Seeding complete. Resetting mechanism...");
  digitalWrite(STATUS_LED, LOW);
  payloadServo.write(POS_LOCKED);
  isSeeding = false;
  delay(1000); // Avoid rapid mechanical cycling
}

void blinkLED(int times) {
  for (int i = 0; i < times; i++) {
    digitalWrite(STATUS_LED, HIGH);
    delay(200);
    digitalWrite(STATUS_LED, LOW);
    delay(200);
  }
}
