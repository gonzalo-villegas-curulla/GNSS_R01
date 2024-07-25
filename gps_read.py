import serial
import time

serial_port = '/dev/ttyS0'  # Change to your serial port
baud_rate   = 9600

try:
    ser = serial.Serial(serial_port, baud_rate, timeout=1)
    print("Serial port opened successfully.")
except serial.SerialException as e:
    print(f"Error opening serial port: {e}")
    exit()

# Function to read and log GNSS data
def read_gnss_data():
    with open('DATA_GPS/gps_data.csv', 'a') as f:
        while True:
            line = ser.readline().decode('ascii', errors='replace').strip()
            if line.startswith('$GPRMC'):
                parts = line.split(',')
                if len(parts) > 9 and parts[2] == 'A':
                    timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())
                    data = [
                        timestamp,
                        parts[1],  # UTC Time
                        parts[2],  # Status
                        parts[3],  # Latitude
                        parts[4],  # Latitude Direction
                        parts[5],  # Longitude
                        parts[6],  # Longitude Direction
                        parts[7],  # Speed
                        parts[8],  # Track Angle
                        parts[9],  # Date
                        parts[10] if len(parts) > 10 else ''  # Magnetic Variation
                    ]
                    f.write(','.join(data) + '\n')
                    f.flush()
                    print("Logged data:", data)
            time.sleep(0.1)

# Start reading and logging GNSS data
read_gnss_data()
