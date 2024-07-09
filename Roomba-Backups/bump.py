import serial

# Open the serial port
ser = serial.Serial('/dev/ttyUSB0', 57600)

# Send the STREAM command to request bumper sensor data
ser.write(bytearray([149, 1, 7]))

while True:
    # Read multiple bytes (assuming we need at least 2 bytes to get meaningful data)
    sensor_data = ser.read(2)
    
    if len(sensor_data) == 2:
        # Combine the bytes into a single integer
        sensor_byte = ord(sensor_data[0]) | (ord(sensor_data[1]) << 8)
        
        # Print the raw byte and its binary representation
        print("Raw Bytes: {}, Combined: {:016b}".format(sensor_data, sensor_byte))
        
        # Extract bumper information from the byte
        bump_right = sensor_byte & 0b00000001
        bump_left = sensor_byte & 0b00000010
        
        # Print the bumper detection status
        if bump_right:
            print("Right bump detected!")
        if bump_left:
            print("Left bump detected!")
