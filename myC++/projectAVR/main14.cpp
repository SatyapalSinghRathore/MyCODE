#define F_CPU 16000000UL
#include <Arduino.h>
#include <HX711.h>
#include <util/delay.h>
#include <LiquidCrystal.h>
#include <Keypad.h>

/* NOTE:- 'delay(time in ms);' it is time delay in arduino framework
, which is not working in proteus simulation, although
 there is no compilation error. that why i'm using '_delay_ms();' function from "util/delay.h" */

LiquidCrystal lcd(7, 6, 5, 4, 3, 2);

const byte ROWS = 4; // four rows
const byte COLS = 3; // three columns
char keys[ROWS][COLS] = {
    {'1', '2', '3'},
    {'4', '5', '6'},
    {'7', '8', '9'},
    {'*', '0', '#'}};

byte rowPins[ROWS] = {8, 9, 10, 11}; // connect to the row pinouts of the keypad
byte colPins[COLS] = {12, 13, 14};   // connect to the column pinouts of the keypad

Keypad keypad = Keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS);

#define Dout 19
#define Sck 18
float calibration_factor = 18029.57;

HX711 scale;

/* Output pins for Buzzer, Process_cpt(it will read pushbotton after process complete for buzzer turn off), 
motorEn_coolingFan(it will control ENable pin of L293D along with cooling Fan), 
flow_control, motor_enable_1, motor_enable_2, 
for controlling clockwise and Anti-clockwise rotation of motor shaft using L293D ic. */
int buzzer = 1, Process_cpt = 15, motor_IN1 = 23, motor_IN2 = 22, motorEn_coolingFan = 21, flow_control = 20, flow_control_KD = 17;

// variables
int y_n, choose;
float CW_fvalue;
int T_value = 0, N_value = 0, WWPC_value = 0, CW_value = 0, mass_flow_g_s = 367;

int delay_ms(unsigned int ms)
{
  /* This is a time delay function in millisecond */

  while (ms > 0)
  {
    _delay_ms(1);
    ms--;
  }
  return 0;
}

void reset_variables()
{
  /* This Function will reset all the variables. */

  T_value = 0;
  N_value = 0;
  WWPC_value = 0;
  CW_value = 0;
}

int concat(char value1, char value2)
{
  /* Function to concatenate
    First, we convert two char values into two integers value, the
    two intergers into one integer(for example: 01 => 1). */

  int value3 = value1;
  int value4 = value2;
  value3 -= 48;
  value4 -= 48;
  char s1[2];
  char s2[2];
  // Convert both the intergers to string
  sprintf(s1, "%d", value3);
  sprintf(s2, "%d", value4);
  // Concatenate both strings
  strcat(s1, s2);
  // Convert the concatenated string to interger
  int value5 = atoi(s1);

  return value5;
}

int keypad_read()
{
  /* This Function will take input from keypad(4x3), it will read 2-digit. */

  int value;
  char key1 = '0', key2 = '0';
  for (int i = 0; i < 2; i++)
  {
    while (true)
    {
      char key = keypad.getKey();
      if (key)
      {
        if (key == '#')
        {
          // buzzer
          digitalWrite(buzzer, HIGH);
          delay_ms(500);
          digitalWrite(buzzer, LOW);
          if (i == 1)
          {
            key2 = key1;
            key1 = '0';
            break;
          }
          break;
        }
        else if (key == '*')
        {
          digitalWrite(buzzer, HIGH);
          delay_ms(500);
          digitalWrite(buzzer, LOW);
          reset_variables();
          setup();
          while (1)
          {
            loop();
          }
        }
        else if (key != '#' && key != '*')
        {
          // buzzer
          digitalWrite(buzzer, HIGH);
          delay_ms(100);
          digitalWrite(buzzer, LOW);
          if (i == 0)
          {
            key1 = key;
            break;
          }
          else if (i == 1)
          {
            key2 = key;
            digitalWrite(buzzer, HIGH);
            delay_ms(500);
            digitalWrite(buzzer, LOW);
            break;
          }
        }
      }
    }
  }
  return value = concat(key1, key2);
}

int motor_operation(int T_time)
{
  /* This function will control motor clockwise and
   anti-clockwise rotation by changing signal at IN1
   and IN2 of L293D ic*/
  int half_rot_time = T_time / 2;
  half_rot_time *= 1000;

  digitalWrite(motor_IN1, HIGH);
  digitalWrite(motor_IN2, LOW);
  delay_ms(half_rot_time); // There is a issue.

  digitalWrite(motor_IN1, LOW);
  digitalWrite(motor_IN2, HIGH);
  delay_ms(half_rot_time); // There is a issue.

  digitalWrite(motor_IN1, LOW);
  digitalWrite(motor_IN2, LOW);
  return 0;
}

int BM_motor_operation(int T_value, int N_value, float WWPC_value)
{
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Process is going");
  lcd.setCursor(0, 1);
  lcd.print("on--------------");

  float time = WWPC_value / mass_flow_g_s;
  int valve_op_time = time * 1000;
  digitalWrite(motorEn_coolingFan, HIGH);
  for (int i = 1; i < N_value; i++)
  {
    motor_operation(T_value);
    digitalWrite(flow_control, HIGH);
    delay_ms(valve_op_time); // there is issue
    digitalWrite(flow_control, LOW);
  }
  motor_operation(T_value);
  digitalWrite(motorEn_coolingFan, LOW);
  // function complete sound
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Process Complete");

  while (true)
  {
    tone(buzzer, 1000);
    delay_ms(1000);
    noTone(buzzer);
    delay_ms(1000);

    if (digitalRead(Process_cpt) == 1)
    {
      break;
    }
  }
  return 0;
}

void lcd_begin(int value1, const String &text1, int value2, const String &text2, int value3, const String &text3, int value4, const String &text4)
{
  /* This Function will print all available operation name and sequance number, in our case,
  we have 4 operation, we can extend. */

  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print(text1);
  lcd.setCursor(0, 1);
  lcd.print(value1);
  lcd.setCursor(4, 0);
  lcd.print(text2);
  lcd.setCursor(4, 1);
  lcd.print(value2);
  lcd.setCursor(8, 0);
  lcd.print(text3);
  lcd.setCursor(8, 1);
  lcd.print(value3);
  lcd.setCursor(12, 0);
  lcd.print(text4);
  lcd.setCursor(12, 1);
  lcd.print(value4);
}

void variables_value_print(const String &text1, int value1, const String &text2, int value2, const String &text3, int value3, const String &text4, int value4)
{
  /* This Function will print user input value. */

  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print(text1);
  lcd.setCursor(0, 1);
  lcd.print(value1);
  lcd.setCursor(4, 0);
  lcd.print(text2);
  lcd.setCursor(4, 1);
  lcd.print(value2);
  lcd.setCursor(8, 0);
  lcd.print(text3);
  lcd.setCursor(8, 1);
  lcd.print(value3);
  lcd.setCursor(13, 0);
  lcd.print(text4);
  lcd.setCursor(13, 1);
  lcd.print(value4);
}

void BM_L_function()
{
  lcd.clear();
  lcd.print("Have you changed");
  lcd.setCursor(0, 1);
  lcd.print("shaft? 1NO 2YES");
  while (true)
  {
    y_n = keypad_read();
    if (y_n == 1)
    {
      /* y_n = 1 it means, answer is 'NO'.( Q.Have you changed shaft? ) */

      lcd.clear();
      lcd.print("Change the shaft");
      lcd.setCursor(0, 1);
      lcd.print("Then.");
    }
    else if (y_n == 2)
    {
      /* y_n = 2 it means, answer is 'YES'.( Q.Have you changed shaft? ) */
      CW_fvalue = scale.get_units() / 2;
      if (CW_fvalue < 0)
      {
        CW_fvalue = 0.0;
      }

      CW_value = int(CW_fvalue);
      variables_value_print("T", T_value, "N", N_value, "WWPC", WWPC_value, "TCW", CW_value);
      T_value = keypad_read();
      variables_value_print("T", T_value, "N", N_value, "WWPC", WWPC_value, "TCW", CW_value);
      N_value = keypad_read();
      variables_value_print("T", T_value, "N", N_value, "WWPC", WWPC_value, "TCW", CW_value);
      WWPC_value = keypad_read();
      variables_value_print("T", T_value, "N", N_value, "WWPC", WWPC_value, "TCW", CW_value);
      // cw_value will be equal to weight sensor data,.
      // SENSOR CODE IS PENDING....
      variables_value_print("T", T_value, "N", N_value, "WWPC", WWPC_value, "TCW", CW_value);
      delay_ms(1000);

      lcd.clear();
      lcd.setCursor(4, 0);
      lcd.print("TWW");
      lcd.setCursor(4, 1);
      lcd.print(WWPC_value * (N_value - 1));
      lcd.setCursor(10, 0);
      lcd.print("TCW");
      lcd.setCursor(10, 1);
      lcd.print(CW_value);
      delay_ms(2000);

      lcd.clear();
      lcd.print("Do you want to");
      lcd.setCursor(0, 1);
      lcd.print("continue? NO/YES");
      y_n = keypad_read();
      if (y_n == 1)
      {
        /* y_n = 1 it means, answer is 'NO'.( Q.Do you want to continue? ) */
        reset_variables();
        break;
      }
      else if (y_n == 2)
      {
        /* y_n = 2 it means, answer is 'YES'.( Q.Do you want to continue? ) */

        // finally, we will call here BM function
        BM_motor_operation(T_value, N_value, WWPC_value);
        reset_variables();
        break;
      }
    }
  }
}

void VC_KD_function()
{
  lcd.clear();
  lcd.print("Have you changed");
  lcd.setCursor(0, 1);
  lcd.print("shaft? 1NO 2YES");
  while (true)
  {
    y_n = keypad_read();
    if (y_n == 1)
    {
      /* y_n = 1 it means, answer is 'NO'.( Q.Have you changed shaft? ) */

      lcd.clear();
      lcd.print("Change the shaft");
      lcd.setCursor(0, 1);
      lcd.print("Then.");
    }
    else if (y_n == 2)
    {
      /* y_n = 2 it means, answer is 'YES'.( Q.Have you changed shaft? ) */

      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("T");
      lcd.setCursor(0, 1);
      lcd.print(T_value);
      T_value = keypad_read();

      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("T");
      lcd.setCursor(0, 1);
      lcd.print(T_value);
      delay_ms(1000);

      lcd.clear();
      lcd.print("Do you want to");
      lcd.setCursor(0, 1);
      lcd.print("continue? NO/YES");
      y_n = keypad_read();
      if (y_n == 1)
      {
        /* y_n = 1 it means, answer is 'NO'.( Q.Do you want to continue? ) */
        reset_variables();
        break;
      }
      else if (y_n == 2)
      {
        /* y_n = 2 it means, answer is 'YES'.( Q.Do you want to continue? ) */
        // There is no special function for VC
        
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print("Process is going");
        lcd.setCursor(0, 1);
        lcd.print("on--------------");

        digitalWrite(motorEn_coolingFan, HIGH);

        digitalWrite(motor_IN1, HIGH);
        digitalWrite(motor_IN2, LOW);
        
        while(T_value != 0){
          if(digitalRead(flow_control_KD) == 1){
            digitalWrite(flow_control, HIGH);
          }
          else {
            digitalWrite(flow_control, LOW);
          }
          T_value--;
          delay_ms(1000);
        }
        
        digitalWrite(motor_IN1, LOW);
        digitalWrite(motor_IN2, LOW);
        digitalWrite(flow_control, LOW);

        digitalWrite(motorEn_coolingFan, LOW);

        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print("Process Complete");

        while (true)
        {
          tone(buzzer, 1000);
          delay_ms(1000);
          noTone(buzzer);
          delay_ms(1000);

          if (digitalRead(Process_cpt) == 1)
          {
            break;
          }
        }
      }
      reset_variables();
      break;
    }
  }
}

void setup()
{
  scale.begin(Dout, Sck);
  scale.set_scale(calibration_factor);
  scale.tare(); // Assuming there is no weight on the scale at start up, reset the scale to 0.

  pinMode(Process_cpt, INPUT);
  pinMode(flow_control_KD, INPUT);

  pinMode(buzzer, OUTPUT);
  pinMode(motor_IN1, OUTPUT);
  pinMode(motor_IN2, OUTPUT);
  pinMode(motorEn_coolingFan, OUTPUT);
  pinMode(flow_control, OUTPUT);
  // pinMode(flow_control_KD, OUTPUT);
  
  digitalWrite(flow_control_KD, LOW);
  lcd.begin(16, 2);
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("----WELCOME----");
  delay_ms(2000);
}

void loop()
{
  lcd.clear();
  lcd_begin(1, "BM", 2, "VC", 3, "L", 4, "KD");
  choose = keypad_read();

  switch (choose)
  {
  case 1:
    lcd.clear();
    lcd.print("---Buttermilk---");
    delay_ms(2000);

    BM_L_function();
    break;

  case 2:
    lcd.clear();
    lcd.print("Vegetable Cutter");
    delay_ms(2000);

    VC_KD_function();
    break;

  case 3:
    lcd.clear();
    lcd.print("-----Lassi!-----");
    delay_ms(2000);

    BM_L_function();
    break;

  case 4:
    lcd.clear();
    lcd.print("--Knead dough--");
    delay_ms(2000);

    VC_KD_function();
    break;

  default:
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("! You have enter");
    lcd.setCursor(0, 1);
    lcd.print(" wrong number.");
    delay_ms(2000);
    break;
  }
}
