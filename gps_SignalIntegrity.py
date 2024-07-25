import serial
import pynmea2
import datetime
import os

def create_log_file():
    """Creates a timestamped log file."""
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"gps_data_{timestamp}.log"
    if not os.path.exists('logs'):
        os.makedirs('logs')
    filepath = os.path.join('logs', filename)
    return open(filepath, 'w')

def parse_gps_data(data):
    """Parses GPS data from the NEO-6M module."""
    try:
        msg = pynmea2.parse(data)
        return msg
    except pynmea2.ParseError as e:
        print(f"Failed to parse GPS data: {e}")
        return None

def log_data(file, data):
    """Logs data to the file."""
    file.write(data + '\n')
    file.flush()

def print_gps_data(msg):
    """Prints basic GNSS data."""
    if isinstance(msg, pynmea2.types.talker.GGA):
        print(f"Timestamp: {msg.timestamp}")
        print(f"Latitude: {msg.latitude} {msg.lat_dir}")
        print(f"Longitude: {msg.longitude} {msg.lon_dir}")
        print(f"Altitude: {msg.altitude} {msg.altitude_units}")
        print(f"Number of Satellites: {msg.num_sats}")
        print(f"Horizontal Dilution of Precision: {msg.horizontal_dil}")
        print(f"Geoidal Separation: {msg.geo_sep} {msg.geo_sep_units}")
    elif isinstance(msg, pynmea2.types.talker.RMC):
        print(f"Timestamp: {msg.timestamp}")
        print(f"Latitude: {msg.latitude} {msg.lat_dir}")
        print(f"Longitude: {msg.longitude} {msg.lon_dir}")
        print(f"Speed Over Ground: {msg.spd_over_grnd}")
        print(f"Track Angle: {msg.true_course}")
        print(f"Date: {msg.datestamp}")
    elif isinstance(msg, pynmea2.types.talker.GSV):
        print(f"Number of Satellites in View: {msg.num_sv_in_view}")
        for i in range(msg.num_sv_in_view):
            print(f"Satellite PRN Number: {msg.sv_prn_num_1}")
            print(f"Elevation: {msg.elevation_deg_1}°")
            print(f"Azimuth: {msg.azimuth_1}°")
            print(f"SNR (C/N0): {msg.snr_1} dB-Hz")

def main():
    # Serial port configuration
    serial_port = '/dev/ttyS0' # /ttyAMA0
    baud_rate = 9600

    # Open serial port
    ser = serial.Serial(serial_port, baud_rate, timeout=1)

    # Create log file
    log_file = create_log_file()

    print("Logging GPS data. Press Ctrl+C to stop.")

    try:
        while True:
            data = ser.readline().decode('ascii', errors='replace').strip()
            if data:
                log_data(log_file, data)
                msg = parse_gps_data(data)
                if msg:
                    print_gps_data(msg)
    except KeyboardInterrupt:
        print("\nLogging stopped.")
    finally:
        log_file.close()
        ser.close()

if __name__ == '__main__':
    main()

