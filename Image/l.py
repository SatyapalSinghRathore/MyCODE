from RPLCD import CharLCD
from time import sleep
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
lcd = CharLCD(numbering_mode=GPIO.BCM, cols=16, rows=2, pin_rs=21, pin_e=20, pins_data=[26,19,13,6])
i=0
while 1:
 lcd.clear()
 lcd.cursor_pos = (0,0)
 lcd.write_string(f'{i}')
 i+=1
 sleep(0.05)
