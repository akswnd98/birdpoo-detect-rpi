import serial
import time

ser = serial.Serial('/dev/ttyACM0', 115200)
time.sleep(2) # 아두이노 리셋 대기

ser.write(b'10000\n')
        
ser.close()
