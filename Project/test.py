#import RPi.GPIO as GPIO
#from RPLCD import CharLCD
#from time import sleep
from Adafruit_Thermal import*
#GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(3, GPIO.OUT)
#while 1:
#   GPIO.output(5, True)
#    sleep(5)
#    GPIO.output(5, False)
#    sleep(5)
#lcd = CharLCD(numbering_mode=GPIO.BOARD, cols=16, rows=2, pin_rs=16, pin_e=18, pins_data=[21,22,24,26])
#lcd.clear()
#lcd.cursor_pos=(0,0)
#lcd.write_string("SSR")
#sleep(5)
#lcd.clear()
#GPIO.output(3, True)
#sleep(0.1)
#GPIO.output(3, False)
#lcd.write_string("SSR")
printer=Adafruit_Thermal("/dev/serial0", 9600, timeout=5)
printer.printImage("/home/pi/Desktop/Project/Apple.png", True)
#printer.print("Satyapal singh rathore")
#for i in range(1,5):
 #printer.print("*\n"*i)
#for i in range(4,0):
#printer.print("-------------------------------\n")
#printer.test()
printer.feed(2)
