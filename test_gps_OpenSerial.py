import serial
import time
ser = serial.Serial('/dev/ttyS0',9600,timeout=1)
line = ser.readline().decode('ascii',errors='replace').strip()
print(line)
