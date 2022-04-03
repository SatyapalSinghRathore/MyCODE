import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.OUT)
while True:
    GPIO.output(40, True)
    time.sleep(0.5)
    GPIO.output(40, False)
    time.sleep(0.5)
