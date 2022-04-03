import RPi.GPIO as GPIO
from RPLCD import CharLCD
from time import sleep
from Adafruit_Thermal import*

winner="Apple"
winner_vote_count=0

apple_m_vote=0
banana_m_vote=0
coconut_m_vote=0

apple_a_vote=0
banana_a_vote=0
coconut_a_vote=0

buzzer=3
relay=5
led=7

R1 = 37
R2 = 35
R3 = 33
R4 = 31

C1 = 29
C2 = 40
#C3 = 36
C4 = 38

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

lcd = CharLCD(numbering_mode=GPIO.BOARD, cols=16, rows=2, pin_rs=16, pin_e=18, pins_data=[21,22,24,26])
printer=Adafruit_Thermal("/dev/serial0", 9600, timeout=5)

GPIO.setup(buzzer, GPIO.OUT)
GPIO.setup(relay, GPIO.OUT)
GPIO.setup(led, GPIO.OUT)

GPIO.setup(R1, GPIO.OUT)
GPIO.setup(R2, GPIO.OUT)
GPIO.setup(R3, GPIO.OUT)
GPIO.setup(R4, GPIO.OUT)

GPIO.setup(C1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# GPIO.setup(C3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


last_vote=['null']

def reset_vote():
    global apple_m_vote,banana_m_vote,coconut_m_vote
    global apple_a_vote,banana_a_vote,coconut_a_vote
    apple_m_vote=0
    banana_m_vote=0
    coconut_m_vote=0

    apple_a_vote=0
    banana_a_vote=0
    coconut_a_vote=0

def last_vote_upt(name):
    last_vote.remove(last_vote[0])
    last_vote.append(name)

def candidate_symbol(name):
    global apple_m_vote,banana_m_vote,coconut_m_vote
    global apple_a_vote,banana_a_vote,coconut_a_vote,winner_vote_count
    if last_vote[0]==name:
        GPIO.output(led, False)
        if name=="Apple":
            apple_a_vote+=1
        elif name=="Banana":
            banana_a_vote+=1
        else:
            coconut_a_vote+=1
        sleep(12)
        GPIO.output(relay, True)
        sleep(10)
        GPIO.output(relay, False)
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
        if winner_vote_count != 0:
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
        GPIO.output(relay, True)
        sleep(10)
        GPIO.output(relay, False)
        sleep(10)

        winner_vote_count=0
        GPIO.output(led, True)

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

def display(line):
    global num,winner_vote_count
    GPIO.output(line, GPIO.HIGH)
    if(GPIO.input(C2) == 1):
        if line==R2:
            GPIO.output(buzzer, True)
            time.sleep(0.1)
            GPIO.output(buzzer, False)
            first()
        elif line==R3:
            GPIO.output(buzzer, True)
            time.sleep(0.1)
            GPIO.output(buzzer, False)
            second()
        else:
            pass
    elif (GPIO.input(C4) == 1):
        if line==R4:
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

def result():
    first()
    while num==2:
        display(R2)
        display(R3)
        display(R4)
        sleep(0.2)

    #print("\n\t\t------------------------------- Result -------------------------------------")
    #print("\n\t\tCandidate\tActual vote\tManipulated votes\tTotal printed receipt")
    #print(f"\n\t\tApple    :\t    {apple_a_vote}\t\t\t{apple_m_vote}\t\t\t{apple_m_vote}")
    #print(f"\n\t\tBanana   :\t    {banana_a_vote}\t\t\t{banana_m_vote}\t\t\t{banana_m_vote}")
    #print(f"\n\t\tCoconut  :\t    {coconut_a_vote}\t\t\t{coconut_m_vote}\t\t\t{coconut_m_vote}")
    #print("\n\t\t----------------------------------------------------------------------------")
    #print(f"\n\t\tTotal    :\t    {total_a_vote}\t\t\t{total_m_vote}\t\t\t{total_m_vote}\n")

def readLine(line, characters):
    global apple_m_vote,banana_m_vote,coconut_m_vote
    global winner
    global num
    GPIO.output(line, GPIO.HIGH)
    if(GPIO.input(C1) == 1):
        if line==R1:
            total_vote = apple_m_vote + banana_m_vote + coconut_m_vote
            if total_vote==0:
                if num==0:
                    GPIO.output(buzzer, True)
                    sleep(0.1)
                    GPIO.output(buzzer, False)
                    winner="Apple"
            else:
                pass
        elif line==R2:
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
        elif line==R3:
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
        else:
            total_vote = apple_m_vote + banana_m_vote + coconut_m_vote
            if total_vote==0:
                if num==0:
                    GPIO.output(buzzer, True)
                    sleep(0.1)
                    GPIO.output(buzzer, False)
                    GPIO.output(led, True)
                    num=1
                else:
                    pass
            else:
                pass

    #if(GPIO.input(C2) == 1):
        #if line==R2:
            #GPIO.output(buzzer, True)
            #time.sleep(0.1)
            #GPIO.output(buzzer, False)
        #elif line==R3:
            #GPIO.output(buzzer, True)
            #time.sleep(0.1)
            #GPIO.output(buzzer, False)
        #else:
            #pass

    #if(GPIO.input(C3) == 1):
        #print(characters[2])
        #GPIO.output(3, True)
        #time.sleep(0.1)
        #GPIO.output(3, False)
    if(GPIO.input(C4) == 1):
        if num==1:
            if line==R4:
                GPIO.output(buzzer, True)
                sleep(0.1)
                GPIO.output(buzzer, False)
                num=2
                GPIO.output(led, False)
                if winner_vote_count != 0:
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

            else:
                GPIO.output(buzzer, True)
                sleep(0.1)
                GPIO.output(buzzer, False)
                candidate_symbol(characters[3])
        else:
            pass

    GPIO.output(line, GPIO.LOW)

lcd.clear()
GPIO.output(led, True)
sleep(3)
GPIO.output(led, False)

num=0

try:
    while True:
        readLine(R1, ["\t1","\t2","\t3","Apple"])
        readLine(R2, ["\t4","\t5","\t6","Banana"])
        readLine(R3, ["\t7","\t8","\t9","Coconut"])
        readLine(R4, ["\t*","\t0","\t#","Done"])
        sleep(0.2)

except KeyboardInterrupt:
    print("\nProgram is stopped")
