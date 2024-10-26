// Define the pin where the sensor is connected
const int sensorPin = A0;

// Variable to store the sensor value
int sensorValue = 0;

void setup() {
    // Initialize serial communication at 9600 bits per second
    Serial.begin(9600);
}

void loop() {
    // Read the value from the sensor
    sensorValue = analogRead(sensorPin);

    // Print the sensor value to the serial monitor
    Serial.print("Soil Moisture Value: ");
    Serial.println(sensorValue);

    // Wait for a second before reading again
    delay(1000);
}