import serial #Serial imported for Serial communication
import time #Required to use delay functions

while True:
    try:
        ArduinoSerial = serial.Serial('com5',9600,timeout = 1)
        break
    except:
        print ("Unable to connect to the device.")
        time.sleep(2)
        continue


def setLight(lane):
    while True:
        try:
            if lane == 1 :
                ArduinoSerial.write(str.encode('1'))
            elif lane ==2:
                ArduinoSerial.write(str.encode('2'))
            elif lane ==3:
                ArduinoSerial.write(str.encode('3'))
            elif lane ==4:
                ArduinoSerial.write(str.encode('4'))
            elif lane==0:
                ArduinoSerial.write(str.encode('0'))
            break

        except:
            print ("Error in communicating to the device...")
            time.sleep (2)
            continue

