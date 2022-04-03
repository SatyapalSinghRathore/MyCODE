from RPLCD import CharLCD
from time import sleep
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(16, GPIO.OUT)
#GPIO.setup(12, GPIO.OUT)
#GPIO.output(16, True)
#GPIO.output(12, True)
lcd = CharLCD(numbering_mode=GPIO.BCM, cols=1, rows=1, pin_rs=21, pin_e=20, pins_data=[26, 19, 13, 6])
lcd.cursor_pos=(0,0)
lcd.write_string(u"S")
