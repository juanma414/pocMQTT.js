import paho.mqtt.client as mqtt
import serial
import time

# Configuración del broker MQTT
mqtt_broker = "test.mosquitto.org"
mqtt_port = 1883
mqtt_topic = "dswHumedad"

# Configuración del puerto serial
serial_port = "COM6"  # Cambia esto según tu configuración
baud_rate = 9600

# Conectar al broker MQTT
client = mqtt.Client()
client.connect(mqtt_broker, mqtt_port, 60)

# Conectar al puerto serial
ser = serial.Serial(serial_port, baud_rate)

try:
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').strip()
            print(f"Datos recibidos: {line}")
            valor = int(line)
            humedad = 100 - (valor / 1023 * 100)
            mensaje = f"Humedad: {humedad:.2f}%"
            print(f"Datos recibidos: {line} - {mensaje}")

            # Publicar los datos en el tópico MQTT
            client.publish(mqtt_topic, mensaje)
            print(f"Datos enviados al tópico {mqtt_topic}")
except KeyboardInterrupt:
    print("Programa terminado")
finally:
    ser.close()
    client.disconnect()
    try:
        while True:
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8').strip()
                print(f"Datos recibidos: {line}")
                
                # Publicar los datos en el tópico MQTT
                client.publish(mqtt_topic, line)
                print(f"Datos enviados al tópico {mqtt_topic}")
            
            # Esperar 1 segundo antes de la siguiente iteración
            time.sleep(1)
    except KeyboardInterrupt:
        print("Programa terminado")
    finally:
        ser.close()
        client.disconnect()    