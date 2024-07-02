import serial

# Open the serial port
ser = serial.Serial('/dev/ttyUSB0', 57600)

# Send the STREAM command
ser.write(bytearray([149, 1, 7]))

while True:
    # Read the sensor data byte
    sensor_data = ser.read(1)
    
    if sensor_data:
        sensor_byte = ord(sensor_data)
        
        bump_right = sensor_byte & 0b00000001
        bump_left = sensor_byte & 0b00000010
        
        if bump_right:
            print("Right bump detected!")
        if bump_left:
            print("Left bump detected!")
