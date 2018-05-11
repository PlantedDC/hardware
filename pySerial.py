import serial
import json
import requests
import datetime

# listen on serial(usb) for arduino communication

ser = serial.Serial('/devttyACM0', 9600)
url = 'https://plant-test.herokuapp.com/addData'

def sendData(data):
    headers = {'content-type': 'application/json'}
    jsondata = json.dumps(data)
    print jsondata
    response = requests.post(url, headers=headers, data=jsondata)
    print (response.text)

while True:
    json_obj = {}
    read_serial = ser.readline()
    data = read_serial.split()
    if data[0] == 'temperature':
        json_obj[data[0]] = data[1]
        read_serial = ser.readline()
        data = read_serial.split()
        json_obj[data[0]] = data[1]

        read_serial = ser.readline()
        data = read_serial.split()
        json_obj[data[0]] = data[1]
        json_obj['time'] = str(datetime.datetime.now())

        sendData(json_obj)

