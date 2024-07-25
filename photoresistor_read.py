import RPi.GPIO as GPIO
import time

# set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)

try:
	while True:
		if GPIO.input(17):
			print("Light level is above the threshold")
		else:
			print("Light level is below the threshold")
		time.sleep(1)
except KeyboardInterrupt:
	GPIO.cleanup()
