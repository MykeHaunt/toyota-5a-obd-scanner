import random
from datetime import datetime

def format_error_list(raw):
    return [{
        'code': item['code'],
        'description': item['desc'],
        'solution': item['sol'],
        'severity': item['sev']
    } for item in raw]

def format_live_data(simulation=True):
    if simulation:
        return {
            'rpm': random.randint(700,3000),
            'coolant_temp': random.randint(80,95),
            'throttle': random.randint(0,100),
            'timestamp': datetime.now().isoformat()
        }
    return {'error':'Hardware not supported'}
