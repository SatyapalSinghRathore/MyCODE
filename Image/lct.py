from RPLCD import CharLCD
from time import sleep
import RPi.GPIO as GPIO


lcd = CharLCD(numbering_mode=GPIO.BCM, cols=16, rows=2, pin_rs=21, pin_e=20, pins_data=[26, 19, 13, 6])
#lcd.cursor_pos = (0, 3)
#lcd.write_string(u'Hello world!')
#sleep(2)
#lcd.clear()
a=1
b=2
c=0
n=4
#i=0

lcd.cursor_pos = (0, 0)
lcd.write_string(u'A')
lcd.cursor_pos = (0, 2)
lcd.cursor_pos = (0, 3)
lcd.write_string(u'B')
lcd.cursor_pos = (0, 6)
lcd.write_string(u'C')
lcd.cursor_pos = (0, 9)
lcd.write_string(u'N')
lcd.cursor_pos = (0, 13)
lcd.write_string(u'TL')

lcd.cursor_pos = (1, 0)
lcd.write_string(f'{a}')
lcd.cursor_pos = (1, 3)
lcd.write_string(f'{b}')
lcd.cursor_pos = (1, 6)
lcd.write_string(f'{c}')
lcd.cursor_pos = (1, 9)
lcd.write_string(f'{n}')
lcd.cursor_pos = (1, 13)
lcd.write_string(f'{a+b+c+n}')
sleep(5)
#lcd.clear()
