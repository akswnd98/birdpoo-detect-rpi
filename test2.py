import time
import serial

ser = serial.Serial('/dev/ttyACM0', 115200)
time.sleep(2)
ser.write(b'10000,10000\n')
ser.close()
    
