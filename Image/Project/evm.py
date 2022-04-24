#This is a Comment.

import RPi.GPIO as GPIO        # This is the Raspberry Pi 4 own Library. We are using 'RPi.GPIO' library as a 'GPIO'(we can give any name), Which is operate all GPIO (Digital Pin) pin.
from RPLCD import CharLCD      # We are using/import(include) 'CharLCD' class from 'RPLCD' library(we can install this library using this terminal command- 'pip install RPLCD'), Which is use to control Liquid Crystal Display (Note:- Only for 16x2 LCD).
from time import sleep         # We are using/import(include) 'sleep' function from 'time'(Python in build library) library, Delay execution for a given number of seconds. The argument may be a floating point number for subsecond precision.
from Adafruit_Thermal import*  # 'Adafruit_Thermal.py' is a Python file, just like this one (evm.py), so We are using this Python file as a Library (Adafruit_Thermal) in evm.py file. which is use to control our Thermal Printer. 

winner="Apple"                 # 'Apple' candidate is our default winner(which is string variable).
winner_vote_count=0            # 'winner_vote_count' is use to count votes for winner, which is initial value '0'. 

apple_m_vote=0                 # 'apple_m_vote'(apple manipulated vote count (integer variable)), which is initial value '0'.
banana_m_vote=0                # 'banana_m_vote'(banana manipulated vote count (integer variable)), which is initial value '0'.
coconut_m_vote=0               # 'coconut_m_vote'(coconut manipulated vote count (integer variable)), which is initial value '0'.

apple_a_vote=0                 # 'apple_a_vote'(apple actual vote count (integer variable)), which is initial value '0'.
banana_a_vote=0                # 'banana_a_vote'(banana actual vote count (integer variable)), which is initial value '0'.
coconut_a_vote=0               # 'coconut_a_vote'(coconut actual vote count (integer variable)), which is initial value '0'.

buzzer=3                       # We are connecting our buzzer to GPIO(Digital pin, GPIO.Board) pin no. 3.
relay=5                        # We are connecting our relay(generate pluse (for bulb ON/OFF)) to GPIO(Digital pin, GPIO.Board) pin no. 5.
led=7                          # We are connecting our led to GPIO(Digital pin, GPIO Board) pin no. 7.

R1 = 37                        # We are connecting our Row1(R1, Keypad) to GPIO(Digital pin, GPIO Board) pin no. 37.
R2 = 35                        # We are connecting our Row2(R2, Keypad) to GPIO(Digital pin, GPIO Board) pin no. 35.
R3 = 33                        # We are connecting our Row3(R3, Keypad) to GPIO(Digital pin, GPIO Board) pin no. 33.
R4 = 31                        # We are connecting our Row4(R4, Keypad) to GPIO(Digital pin, GPIO Board) pin no. 31.

C1 = 29                        # We are connecting our Column1(C1, Keypad) to GPIO(Digital pin, GPIO Board) pin no. 37.
C2 = 40                        # We are connecting our Column2(C1, Keypad) to GPIO(Digital pin, GPIO Board) pin no. 37.
C4 = 38                        # We are connecting our Column4(C1, Keypad) to GPIO(Digital pin, GPIO Board) pin no. 37.

GPIO.setwarnings(False)        # 'setwarnings' is a function from 'GPIO' library, which is control our warning message.
GPIO.setmode(GPIO.BOARD)       # 'setmode' is a function, 'GPIO' (RPi.GPIO) library has Two modes: GPIO.BCM and GPIO.BOARD. you can use either pin number (BOARD) or the Broadcom GPIO number (BCM), but you can only use one system in each program.

lcd = CharLCD(numbering_mode=GPIO.BOARD, cols=16, rows=2, pin_rs=16, pin_e=18, pins_data=[21,22,24,26])  # Here, we are setup our LCD(16X2) display connection, where 'rs' is connected to 16, 'en' is connected to 18, and D4=21, D5=22, D6=24, D7=26 (D is lcd data pin).
printer=Adafruit_Thermal("/dev/serial0", 9600, timeout=5)      # Here, we are setup our Thermal printer connection, where '/dev/serial0' define our TTL(TX, Rx, GND) connection (Not sure!) and 9600 is our printer baudrate (Note:- our Thermal Printer(PNP-500 model) has 9600 baudrate, That's why 9600).

GPIO.setup(buzzer, GPIO.OUT)   # We are using buzzer pin as an OUTPUT.
GPIO.setup(relay, GPIO.OUT)    # We are using relay pin as an OUTPUT.
GPIO.setup(led, GPIO.OUT)      # We are using led pin as an OUTPUT.

GPIO.setup(R1, GPIO.OUT)       # We are using Row1 pin as an OUTPUT.
GPIO.setup(R2, GPIO.OUT)       # We are using Row2 pin as an OUTPUT.
GPIO.setup(R3, GPIO.OUT)       # We are using Row3 pin as an OUTPUT.
GPIO.setup(R4, GPIO.OUT)       # We are using Row4 pin as an OUTPUT.

GPIO.setup(C1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)    # We are using Column1 pin as pull_down. (There is our winner key(using this key we can change our winner, otherwise default winner is 'Apple') located)
GPIO.setup(C2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)    # We are using Column2 pin as pull_down. (There is our Up(apple and banana data) and Down(coconut and Total vote data) key( for result data) located for LCD(16x2) display)
GPIO.setup(C4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)    # We are using Column4 pin as pull_down. (There is our all candidate symbols(Apple, Banana and Coconut) and Done key located)


last_vote=['null']             # It will store our last vote(by user/voter), and it will update according to last vote, which is help us for manipulation.


'''
For better understanding, you should read code from line no. 337.
'''


'''
This function will reset('0') our all Manipulated and Actual votes for new voting.
'''
def reset_vote():
    global apple_m_vote,banana_m_vote,coconut_m_vote
    global apple_a_vote,banana_a_vote,coconut_a_vote
    apple_m_vote=0
    banana_m_vote=0
    coconut_m_vote=0

    apple_a_vote=0
    banana_a_vote=0
    coconut_a_vote=0


'''
This function will update our last_vote. As I told in Line 55. and 
'name' is a function arrgument, it can be apple/banana/coconut.
'''
def last_vote_upt(name):
    last_vote.remove(last_vote[0])
    last_vote.append(name)


'''
This function will print our candidate symbole/Image on thermal 
paper and count manipulated and Actual vote according to canditions, 
and 'name' is a function arrgument, it can be apple/banana/coconut 
(it will print image according to arrgument).
'''
def candidate_symbol(name):
    global apple_m_vote,banana_m_vote,coconut_m_vote
    global apple_a_vote,banana_a_vote,coconut_a_vote,winner_vote_count
    if last_vote[0]==name:    # When last vote is equal to current vote.
        GPIO.output(led, False)
        if name=="Apple":
            apple_a_vote+=1
        elif name=="Banana":
            banana_a_vote+=1
        else:
            coconut_a_vote+=1
        sleep(12)
        GPIO.output(relay, False)
        sleep(10)
        GPIO.output(relay, True)
        if winner=="Apple":
            apple_m_vote+=1
        elif winner=="Banana":
            banana_m_vote+=1
        else:
            coconut_m_vote+=1

        winner_vote_count+=1
        GPIO.output(led, True)

    else:
        GPIO.output(led, False)
        if winner_vote_count != 0:   # It will print the remaining manipulated vote in backgroud(without informing the voter).
            for i in range(0,winner_vote_count):
               printer.printImage(f"/home/pi/Desktop/Project/{winner}.png", True)
               printer.feed(1)
               printer.print("-------------------------------")
               printer.feed(1)
        last_vote_upt(name)
        printer.printImage(f"/home/pi/Desktop/Project/{name}.png", True)
        printer.feed(1)
        printer.print("-------------------------------")
        printer.feed(1)
        if name=="Apple":
            apple_m_vote+=1
            apple_a_vote+=1
        elif name=="Banana":
            banana_m_vote+=1
            banana_a_vote+=1
        else:
            coconut_m_vote+=1
            coconut_a_vote+=1
        GPIO.output(relay, False)
        sleep(10)
        GPIO.output(relay, True)
        sleep(10)

        winner_vote_count=0
        GPIO.output(led, True)


'''
This function will display Apple and Banana- actual vote,
 manipulate vote and printed reciept/manipulate vote( because
 manipulate vote is equal to printed reciept) on LCD(16x2).
'''
def first():
    total_m_vote = apple_m_vote + banana_m_vote + coconut_m_vote
    total_a_vote = apple_a_vote + banana_a_vote + coconut_a_vote
    lcd.clear()
    lcd.cursor_pos = (0,0)
    lcd.write_string("APPLE")
    lcd.cursor_pos = (0,8)
    lcd.write_string(f"{apple_a_vote}")
    lcd.cursor_pos = (0,11)
    lcd.write_string(f"{apple_m_vote}")
    lcd.cursor_pos = (0,14)
    lcd.write_string(f"{apple_m_vote}")
    lcd.cursor_pos = (1,0)
    lcd.write_string("BANANA")
    lcd.cursor_pos = (1,8)
    lcd.write_string(f"{banana_a_vote}")
    lcd.cursor_pos = (1,11)
    lcd.write_string(f"{banana_m_vote}")
    lcd.cursor_pos = (1,14)
    lcd.write_string(f"{banana_m_vote}")


'''
This function will display Coconut and Total- actual vote,
manipulate vote and printed reciept/manipulate vote( because
manipulate vote is equal to printed reciept) on LCD(16x2).
'''
def second():
    total_m_vote = apple_m_vote + banana_m_vote + coconut_m_vote
    total_a_vote = apple_a_vote + banana_a_vote + coconut_a_vote
    lcd.clear()
    lcd.cursor_pos = (0,0)
    lcd.write_string("COCONUT")
    lcd.cursor_pos = (0,8)
    lcd.write_string(f"{coconut_a_vote}")
    lcd.cursor_pos = (0,11)
    lcd.write_string(f"{coconut_m_vote}")
    lcd.cursor_pos = (0,14)
    lcd.write_string(f"{coconut_m_vote}")
    lcd.cursor_pos = (1,0)
    lcd.write_string("TOTAL")
    lcd.cursor_pos = (1,8)
    lcd.write_string(f"{total_a_vote}")
    lcd.cursor_pos = (1,11)
    lcd.write_string(f"{total_m_vote}")
    lcd.cursor_pos = (1,14)
    lcd.write_string(f"{total_m_vote}")


'''This function will read 'UP' button(UP icon on keypad, at location C2 column and R2)
 and 'DOWN' button(DOWN icon on keypad, at location C2 column and R3 row),
  so that we can display our vote on LCD(16x2) in two parts(which is our first() and second() function).
'''
def display(line):
    global num,winner_vote_count
    GPIO.output(line, GPIO.HIGH)
    if(GPIO.input(C2) == 1):
        if line==R2:    # This is our 'UP' button on keypad.
            GPIO.output(buzzer, True)
            time.sleep(0.1)
            GPIO.output(buzzer, False)
            first()
        elif line==R3:  # This is our 'DOWN' button on keypad.
            GPIO.output(buzzer, True)
            time.sleep(0.1)
            GPIO.output(buzzer, False)
            second()
        else:
            pass
    elif (GPIO.input(C4) == 1):
        if line==R4:    # This is our 'Done' button on keypad. LCD will be cleared with this button.
            GPIO.output(buzzer, True)
            time.sleep(0.1)
            GPIO.output(buzzer, False)
            reset_vote()
            last_vote_upt("null")
            lcd.clear()
            winner_vote_count=0
            num=0
        else:
            pass

    GPIO.output(line, GPIO.LOW)


'''When we press Done('D' on keypad) button on keypad, this function will execute.'''
def result():
    first()
    while num==2:
        display(R2)
        display(R3)
        display(R4)
        sleep(0.2)


'''This function will read our C1 and C4 according to 'num' variable.'''
def readLine(line, characters):
    global apple_m_vote,banana_m_vote,coconut_m_vote
    global winner
    global num
    GPIO.output(line, GPIO.HIGH)
    if(GPIO.input(C1) == 1):  # When C1(input pin) is HIGH, then we can choose our winner.
        if line==R1:          # This is our '1.' button on keypad.
            total_vote = apple_m_vote + banana_m_vote + coconut_m_vote
            if total_vote==0:
                if num==0:
                    GPIO.output(buzzer, True)
                    sleep(0.1)
                    GPIO.output(buzzer, False)
                    winner="Apple"
            else:
                pass
        elif line==R2:        # This is our '2.' button on keypad.
            total_vote = apple_m_vote + banana_m_vote + coconut_m_vote
            if total_vote==0:
                if num==0:
                    GPIO.output(buzzer, True)
                    sleep(0.1)
                    GPIO.output(buzzer, False)
                    winner="Banana"
                else:
                    pass
            else:
                pass
        elif line==R3:       # This is our '3.' button on keypad.
            total_vote = apple_m_vote + banana_m_vote + coconut_m_vote
            if total_vote==0:
                if num==0:
                    GPIO.output(buzzer, True)
                    sleep(0.1)
                    GPIO.output(buzzer, False)
                    winner="Coconut"
                else:
                    pass
            else:
                pass
        else:                 # So, now R4 only left, which is our 'Ok' button on keypad, it will set our winner and num=1(it means, it will read only C4 column)
            total_vote = apple_m_vote + banana_m_vote + coconut_m_vote
            if total_vote==0:
                if num==0:
                    GPIO.output(buzzer, True)
                    sleep(0.1)
                    GPIO.output(buzzer, False)
                    GPIO.output(led, True)  # It will indicate to voter, now you can vote.
                    num=1
                else:
                    pass
            else:
                pass

    if(GPIO.input(C4) == 1):    # When C4(input pin) is HIGH, then voter can choose own candidate.
        if num==1:
            if line==R4:        # This is our 'Done' button on keypad. voting will be closed with this button.   
                GPIO.output(buzzer, True)
                sleep(0.1)
                GPIO.output(buzzer, False)
                num=2
                GPIO.output(led, False)
                if winner_vote_count != 0:  # Before showing the result, it will print the remaining manipulated vote in backgroud(without informing the voter).
                    for i in range(0,winner_vote_count):
                        printer.printImage(f"/home/pi/Desktop/Project/{winner}.png", True)
                        printer.feed(1)
                        printer.print("-------------------------------")
                        printer.feed(1)
                else:
                    pass
                total_vote1 = apple_m_vote + banana_m_vote + coconut_m_vote
                if total_vote1 != 0:
                    printer.feed(27)
                else:
                    pass
                sleep(2)
                lcd.write_string("-----RESULT-----")
                sleep(2)
                result()

            else:            # This will excute for R1/R2/R3(Apple,banana,coconut respectively). and it will call our candidate_symbol() function.
                GPIO.output(buzzer, True)
                sleep(0.1)
                GPIO.output(buzzer, False)
                candidate_symbol(characters[3])
        else:
            pass

    GPIO.output(line, GPIO.LOW)

# Our Raspberry pi start excuting code from here.
GPIO.output(relay, True)   # This will set our relay pin LOW, so that Light off in VVPAT.
lcd.clear()                # This will clear all data showing on LCD display.
GPIO.output(led, True)     # Here, once our Led blinks, we will know that our code has been run.
sleep(3)
GPIO.output(led, False)


'''
'num' is our integer variable, which is help us to read one 
Column(C1/C2/C4) at a time. (In our case: When num=0, then 
we can only read C1 column(at that column, we choose our 
winner(1./2./3.)) on keypad. When num=1, then we can only 
read C4 column(at that column, voter choose own 
Candidate(Apple/Banana/Coconut)) on keypad. When num=2, 
then we can only read C2 column(at that column, we choose 
our 'UP' and 'DOWN' button(1./2./3.)) on keypad, to show 
all votes on LCD display in two parts.)
'''
num=0

try:
    while True:
        readLine(R1, ["\t1","\t2","\t3","Apple"])        # readLine() function will read our C1 and C4 according to 'num' variable.
        readLine(R2, ["\t4","\t5","\t6","Banana"])
        readLine(R3, ["\t7","\t8","\t9","Coconut"])
        readLine(R4, ["\t*","\t0","\t#","Done"])
        sleep(0.2)

except KeyboardInterrupt:
    print("\nProgram is stopped")
