#include <Servo.h>


Servo S1;
Servo S2;

const int inPin = 3;
const int sensorPin = A0;
int lightVal;

#define fovAngle 60
signed int x = 90 - (fovAngle/2);
signed int y = 90 - (fovAngle/2);
signed char dx = 1;
signed char dy = 1;

bool active = false;

void setup() {

  S1.attach(9);  // x
  S2.attach(10); // y

  BT.begin(9600);

  S1.write(x);
  S2.write(y);

}

void loop() {

  // Read commands.
  while (BT.available())
  {
    String a = BT.readString();
    BT.println(a);
    if (a[0] == 'q')
    {
      x = 90 - (fovAngle/2);
      y = 90 - (fovAngle/2);
      dx = 1;
      dy = 1;
      active = false;
      BT.println("Stopping");
    }
    else if (a[0] == 'p')
    {
      active = false;
      BT.println("Pausing");
    }
    else if (a[0] == 's')
    {
      active = true;
      BT.println("Starting");
    }
  }

  // Read the light, command the servo and transmit the info if active.
  if (active)
  {
    
    S1.write(x);
    S2.write(y);

    x += dx;
    if (x >= (90 + (fovAngle/2)) || x <= (90 - (fovAngle/2)))
    {
      dx *= -1;
      y += dy;
      if (y >= (90 + (fovAngle/2)) || y <= (90 - (fovAngle/2)))
      {
        dy *= -1;
      }
    }

    lightVal = analogRead(sensorPin);
    BT.print(x);
    BT.print(", ");
    BT.print(y);
    BT.print(", ");
    BT.println(lightVal);

  }

  delay(50);

}
