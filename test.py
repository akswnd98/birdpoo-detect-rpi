import serial

ser = serial.Serial('/dev/ttyACM0', 9600)
while True:
    data = ser.read()
    print(data)

ser.close()
