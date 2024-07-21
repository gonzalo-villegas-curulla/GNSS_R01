import serial
import time
from datetime import datetime

# Configure the serial connection to the GPS module
serial_port = "/dev/ttyAMA0" #"/dev/serial0", or "/dev/ttyAMA0", or "/dev/ttyS0" depending on your setup
baud_rate   = 9600
ser         = serial.Serial(serial_port, baud_rate, timeout=1)

# Function to parse NMEA sentences
def parse_nmea(sentence):
    parts = sentence.split(',') # FORMATTING
    if parts[0] == '$GPRMC':
        utc_time            = parts[1]
        status              = parts[2]
        latitude            = parts[3]
        latitude_dir        = parts[4]
        longitude           = parts[5]
        longitude_dir       = parts[6]
        speed_over_ground   = parts[7]
        track_angle         = parts[8]
        date                = parts[9]
        magnetic_variation = parts[10] if len(parts) > 10 else ''
        return {
            'utc_time': utc_time,
            'status': status,
            'latitude': latitude,
            'latitude_direction': latitude_dir,
            'longitude': longitude,
            'longitude_direction': longitude_dir,
            'speed_over_ground': speed_over_ground,
            'track_angle': track_angle,
            'date': date,
            'magnetic_variation': magnetic_variation
        }
    return None

# Log GNSS data to a file every specified period
log_interval  = 2 # [s]
log_file_path = "dataGPS/gps_data.csv"

with open(log_file_path, 'a') as log_file:
    log_file.write("Timestamp,UTC Time,Status,Latitude,Latitude Direction,Longitude,Longitude Direction,Speed,Track Angle,Date,Magnetic Variation\n")

    while True:
        line = ser.readline().decode('ascii', errors='replace').strip()
        if line.startswith('$GPRMC'):
            data = parse_nmea(line)
            if data and data['status'] == 'A':  # 'A' means data is valid
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                log_entry = f"{timestamp},{data['utc_time']},{data['status']},{data['latitude']},{data['latitude_dir']},{data['longitude']},{data['longitude_dir']},{data['speed_over_ground']},{data['track_angle']},{data['date']},{data['magnetic_variation']}\n"
                log_file.write(log_entry)
                log_file.flush()
                print(log_entry.strip())
        time.sleep(log_interval)
