# Hardware
---
## Components
### Single Board Computers and Microcontrollers
* Raspberry Pi 3 model B
* Arduino Uno

### Sensors

---
## Goal
Collect data from a variety of sensors. The Arduino is used because it can
deal with both analogue and digital sensors. The Arduino simply reads data
from the sensors at a set time interval and then transmits this data 
through serial communication to a Raspberry Pi. The Pi takes this data,
puts it into JSON form, and sends it through POST requests to a server
deployed on Heroku. 
