import os

# Toggle between simulation and hardware mode by default
SIMULATION_MODE = True
HARDWARE_PORT   = os.getenv('HARDWARE_PORT', '/dev/ttyUSB0')
HARDWARE_BAUD   = int(os.getenv('HARDWARE_BAUDRATE', 9600))
DATABASE_FILE   = os.getenv('DATABASE_FILE', 'data/diagnostic_logs.db')
LOG_LEVEL       = os.getenv('LOG_LEVEL', 'INFO')
