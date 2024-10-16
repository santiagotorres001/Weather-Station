'''
Script description:
Get temperature and humidity from DHT11 since Arduino.
Date: 07/10/2024
Developer: Santiago Torres
'''
#Import libraries
import serial
import time

#Arduino port
arduino_port = "COM9"
arduino_bau = 9600

service = serial.Serial(
    arduino_port,
    arduino_bau,
    timeout = 1
)

time.sleep(1) #Delay

while True:
    #data = service.readline.decode('utf-8').strip()
    data = service.readline().decode('utf-8').rstrip()
    
    if data:
        print(data)
        #temp, hum = data.split(",")
        
       # print(f"Temperature: {temp} °C")
        #print(f"Humidity: {hum} %")
time.sleep(1)