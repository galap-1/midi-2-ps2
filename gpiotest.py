import time


try:
		import RPi.GPIO as GPIO
except RuntimeError:
	print("Error. Try running with sudo")
	
GPIO.setmode(GPIO.BOARD)

GPIO.setup(12, GPIO.OUT, initial = 0)

EndTime = time.time() + 1
counter = 0

while time.time() < EndTime:

	GPIO.output(12, 1)
	time.sleep(0.00005)
	GPIO.output(12, 0)
	counter = counter + 1
	

GPIO.cleanup()

print (counter)
