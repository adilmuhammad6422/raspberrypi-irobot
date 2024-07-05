import serial

# Open the serial port
ser = serial.Serial('/dev/ttyUSB0', 57600)

# Send the STREAM command
ser.write(bytearray([149, 1, 7]))

while True:
    # Attempt to read a byte
    sensor_data = ser.read(1)
    
    if sensor_data:
        # Convert the byte to an integer
        sensor_byte = ord(sensor_data)
        
        # Print the raw byte and its binary representation
        print("Raw Byte: "+ sensor_byte + ", Binary: "+ sensor_byte + ":08b}")
        
        # Extract bumper information from the byte
        bump_right = sensor_byte & 0b00000001
        bump_left = sensor_byte & 0b00000010
        
        # Print the bumper detection status
        if bump_right:
            print("Right bump detected!")
        if bump_left:
            print("Left bump detected!")
