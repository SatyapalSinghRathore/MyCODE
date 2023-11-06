// #include <Arduino.h>

int Total_Cycle(int No_of_Cycle);
void Clockwise();
void Anti_Clockwise();

//         ----------------[ User Input ]-------------------

int No_of_Steps = 20; // Total Steps in one cycle.
float PPS = 30;      // Pulse per Seconds(PPS).
int No_of_Cycle = 3;
int Motor_OFF_time = 5; // Stepper motroe OFF delay Time(s).

//         -----------------------------------------------

float OP_time_s = (1 / PPS) * 1000; //  One pulse Time(s)
int OP_time = (int)OP_time_s;       //  One pulse Time(ms)

// Pin define
int EN = 4;                               // IC Enable pin
int phasePins[] = {3, 2, 10, 5};          // A, A_, B, B_
int Index_F[] = {0, 1, 2, 3, 1, 0, 3, 2}; // Forward rotation -Pins index NOTE:- If steps in Even 2
int Index_R[] = {2, 3, 0, 1, 3, 2, 1, 0}; // Reverse rotation -Pins index NOTE:- If steps in Even 2

int i = 0;
int odd = 0;

void setup()
{
  // Serial.begin(9600);
  for (int j = 0; j < 4; j++)
  {
    pinMode(phasePins[j], OUTPUT);
  }
  pinMode(EN, OUTPUT);

  // starting position.
  digitalWrite(3, HIGH);
  digitalWrite(2, LOW);
  digitalWrite(10, HIGH);
  digitalWrite(5, LOW);
  digitalWrite(EN, LOW);

  Total_Cycle(No_of_Cycle);
}

int Total_Cycle(int No_of_Cycle)
{
  for (int l = 0; l < No_of_Cycle; l++)
  {
    digitalWrite(EN, HIGH);

    Clockwise();
    // Serial.println("Clock_out"); //-------

    digitalWrite(EN, LOW);
    delay(Motor_OFF_time * 1000);
    digitalWrite(EN, HIGH);

    Anti_Clockwise();
    // Serial.println("Anti_out"); //--------

    digitalWrite(EN, LOW);
    delay(Motor_OFF_time * 1000);
  }
  return 0;
}

void loop()
{
//   digitalWrite(EN, HIGH);

//   Clockwise();
//   // Serial.println("Clock_out"); //-------

//   digitalWrite(EN, LOW);
//   delay(Motor_OFF_time * 1000);
//   digitalWrite(EN, HIGH);

//   Anti_Clockwise();
//   // Serial.println("Anti_out"); //--------

//   digitalWrite(EN, LOW);
//   delay(Motor_OFF_time * 1000);
}

void Clockwise()
{
  int count = 0;
  while (count != No_of_Steps)
  {
    delay(OP_time);
    digitalWrite(phasePins[Index_F[i]], LOW);
    i += 1;
    digitalWrite(phasePins[Index_F[i]], HIGH);
    i += 1;
    count += 1;
    // Serial.print(count);
    // Serial.print(" Fw_step - Complete  ---  ");
    // Serial.print(Index_F[i - 2]);
    // Serial.println(Index_F[i - 1]);

    if (i == 8)
    {
      i = 0;
    }
  }
  delay(10);
}

void Anti_Clockwise()
{
  int count = 0;
  if (No_of_Steps % 2 != 0)
  {
    for (int k = 0; k < 4; k++)
    {
      i += 1;
      if (i == 8)
      {
        i = 0;
      }
    }
  }
  while (count != No_of_Steps)
  {
    digitalWrite(phasePins[Index_R[i]], LOW);
    i += 1;
    digitalWrite(phasePins[Index_R[i]], HIGH);
    delay(OP_time);
    i += 1;
    count += 1;
    // Serial.print(count);
    // Serial.print(" RW_step - Complete  ---  ");
    // Serial.print(Index_R[i - 2]);
    // Serial.println(Index_R[i - 1]);
    if (i == 8)
    {
      i = 0;
    }
  }
  delay(10);
}
