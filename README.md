# photo_resistor

A mono-pixel photo camera.

## Getting Started

First of all, you need to get the circuit set up. I have used a nano, but you could use any other compatible controller. It's too much effort to create a schematic diagram of the connection, so I will just list the Pin Name to device mapping.

```
Photoresistor: A0
HC05 TX: 5
HC05 RX: 4
Servo X: 9
Servo Y: 10
```

Secondly, the main python script to run is `process.py`. Before you run the script do note that you need to identify the bluetooth devive from you serial devices list which can be found by `ll /dev/tty.*` and update this value in `process.py`.

Note that I have tried this on MacOS Mojave, but it should work just fine on any Mac or Linux as long as you can identify the serial device correctly.

## Dependencies

1. Numpy
2. Matplotlib