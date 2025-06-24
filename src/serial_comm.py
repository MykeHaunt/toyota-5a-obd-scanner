import random, time, serial
from threading import Lock

ERROR_CODES = {
    '12': {'desc': 'RPM No NE signal', 'sol': 'Check wiring', 'sev': 'critical'},
    # …add other codes here…
}

_serial_lock = Lock()

def read_codes(port, baudrate, simulation=True, timeout=3):
    if simulation:
        # simulate 0–3 random codes
        avail = list(ERROR_CODES.keys())
        count = random.choices([0,1,2,3], weights=[40,30,20,10])[0]
        codes = random.sample(avail, k=count)
    else:
        try:
            with _serial_lock, serial.Serial(port, baudrate, timeout=timeout) as ser:
                ser.write(b'INIT\r\n'); time.sleep(0.2)
                ser.write(b'CODES\r\n'); time.sleep(0.5)
                resp = ser.readline().decode().strip()
                codes = resp.split(',') if resp and resp!='NO_CODES' else []
        except Exception as e:
            return [{'code':'HW_ERR','desc':str(e),'sol':'Check connection','sev':'critical'}]
    return [{'code':c, **ERROR_CODES[c]} for c in codes]

def clear_codes(port, baudrate, simulation=True):
    if simulation:
        return True
    try:
        with _serial_lock, serial.Serial(port, baudrate, timeout=3) as ser:
            ser.write(b'CLEAR\r\n'); time.sleep(1)
            return ser.readline().decode().strip()=='OK'
    except:
        return False
