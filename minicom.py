import serial
import time
from datetime import datetime
sttime = datetime.now().strftime('%Y%m%d_%H:%M:%S - ')

#ser = serial.Serial('/dev/ttyUSB2', 115200, timeout=1, exclusive=True, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, rtscts=True)
ser = serial.Serial('/dev/ttyUSB2', baudrate=115200)
ser.write(b'AT+CGPSINFO\r\n')
time.sleep(0.5)
response=ser.read_all().decode('utf-8')
#response=ser.read().decode('utf-8')
#response = ser.readline().decode('utf-8')
print(response)

with open('gpsreturn.txt','a') as text:
    text.write(response+sttime + '------------' + '\n')



"""
##enable gps
ser.write(b'AT+CGPS?\r\n')
time.sleep(0.5)
response=ser.read_all().decode('utf-8')
print(response)
with open('gpsreturn.txt','a') as text:
    text.write(response + '------------' + '\n')

ser.write(b'AT+CGPS=1,1\r\n')
time.sleep(0.5)
response=ser.read_all().decode('utf-8')
print(response)
with open('gpsreturn.txt','a') as text:
    text.write(response + '------------' + '\n')

ser.write(b'AT+CGPS?\r\n')
time.sleep(0.5)
response=ser.read_all().decode('utf-8')
print(response)
with open('gpsreturn.txt','a') as text:
    text.write(response + '------------' + '\n')
"""
ser.close()
