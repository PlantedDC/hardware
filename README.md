# Hardware
---
## Components
### Single Board Computers and Microcontrollers
* Raspberry Pi 3 model B
* Arduino Uno

### Sensors

---
## Setup
* Download Arduino IDE from [here](https://www.arduino.cc/en/Main/Software).

   The IDE allows for easy uploading of programs to the Arduino via USB
* Prepare the Raspberry PI.
    - Download Raspbian from [here](https://www.raspberrypi.org/downloads/raspbian/).

   Raspbian is an Debian based version of Linux optimized for the Raspberry Pi hardware.
    - Write the Raspbian image to a microSD card

   A good tool to write the image for Mac OS is [Etcher](https://etcher.io/)

## Goal
Collect data from a variety of sensors. The Arduino is used because it can
deal with both analog and digital sensors. The Arduino simply reads data
from the sensors at a set time interval and then transmits this data 
through serial communication to a Raspberry Pi. The Pi takes this data,
puts it into JSON form, and sends it through POST requests to a server
deployed on Heroku.
