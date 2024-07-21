import board
import busio
import time
from adafruit_bme280 import basic as adafruit_bme280

# Create the I2C bus interface
i2c = busio.I2C(board.SCL, board.SDA)

# Create the BME280 object
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c, address=0x76)

# Optionally, you can set the sea level pressure (default is 1013.25 hPa)
# bme280.sea_level_pressure = 1013.25


try:
	# open the file in write mode
	with open('/home/gvc/Desktop/Projects/SensorData/data/temphumpress.csv','w') as file:
		# write header
		file.write('Timestamp, Temperature(C), Humidity(%),Pressure(hPa)\n')
		try:
			while True:
				# read sensor data
				temp  = bme280.temperature
				hum   = bme280.humidity
				press = bme280.pressure

				# get the current time:
				timestamp = time.strftime('%Y-%m-%d %H:%M:%S')

				# write data to file
				file.write(f'{timestamp},{temp:.2f},{hum:.2f},{press:.2f}\n')
				file.flush() # ensure data is written immediately

				# print data to the console
				print(f'Time: {timestamp}, Temperature:{temp:.2f} C, Humidity: {hum:.2f} %, Pressure: {press:.2f} hPa')
				# sleep for 2 seconds
				time.sleep(60)
		except KeyboardInterrupt:
			print("Data logging stopped.")
except Exception as e:
	print(f"Failed to open or write to file: {e}")

#while True:
#    temperature = bme280.temperature
#    humidity = bme280.humidity
#    pressure = bme280.pressure

#    print(f'Temperature: {temperature:.2f} C')
#    print(f'Humidity: {humidity:.2f} %')
#    print(f'Pressure: {pressure:.2f} hPa')
#    print('---')
    
#    time.sleep(2)
