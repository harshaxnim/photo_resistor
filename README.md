# photo_resistor

Etymology:

**photo_resistor**

*n.*

*A device that takes a photo from a photo-resistor, hence the name, photo_resistor.*

(100 points for the truly ingenious name!)

A **mono-pixel** camera built using a single photo-resistor, two servos and an Arduino Uno.

Of course, the output is hardly photogenic. Here's a sample:

![Sample Output](http://life.inspirho.in/wp-content/uploads/2020/03/interlacingIssue.png)

Read my blog-post describing the build-process here: http://life.inspirho.in/diy/photo-resistor/

## Getting Started

First of all, you need to get the circuit set up. I have used a nano, but you could use any other compatible controller. I am too lazy to create a schematic diagram of the connections, so I will just list the pins-to-device mapping.

```
Photoresistor: A0
HC05 TX: 5
HC05 RX: 4
Servo X: 9
Servo Y: 10
```

Secondly, the main python script to run is `process.py`. Before you run the script do note that you need to identify the bluetooth device from you serial devices list which can be found by `ll /dev/tty.*` (could be different for you) and update this value in `process.py`.

Note that I have tried this on MacOS Mojave, but it should work just fine on any Mac or Linux as long as you can identify the serial device correctly.

## Dependencies

1. Numpy
2. Matplotlib
