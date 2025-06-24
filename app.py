from flask import Flask, jsonify, render_template
import logging

import config
from src.serial_comm import read_codes, clear_codes
from src.database   import init_db, log_session, fetch_history
from src.models     import format_error_list, format_live_data

app = Flask(__name__)
logging.basicConfig(level=config.LOG_LEVEL)
logger = logging.getLogger(__name__)

# Initialize database on startup
init_db(config.DATABASE_FILE)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan')
def scan_ecu():
    codes = read_codes(
        port=config.HARDWARE_PORT,
        baudrate=config.HARDWARE_BAUD,
        simulation=config.SIMULATION_MODE
    )
    errors = format_error_list(codes)
    session_id = log_session(
        mode=('simulation' if config.SIMULATION_MODE else 'hardware'),
        codes=errors,
        db_file=config.DATABASE_FILE
    )
    return jsonify({
        'errors': errors,
        'mode':  'simulation' if config.SIMULATION_MODE else 'hardware',
        'session_id': session_id
    })

@app.route('/clear_codes', methods=['POST'])
def clear_codes_route():
    success = clear_codes(
        port=config.HARDWARE_PORT,
        baudrate=config.HARDWARE_BAUD,
        simulation=config.SIMULATION_MODE
    )
    # Log even clear operations
    log_session(
        mode=f'clear_{"sim" if config.SIMULATION_MODE else "hw"}',
        codes=[],
        db_file=config.DATABASE_FILE
    )
    return jsonify({'success': success})

@app.route('/live_data')
def live_data():
    data = format_live_data(simulation=config.SIMULATION_MODE)
    return jsonify(data)

@app.route('/diagnostic_history')
def diagnostic_history():
    sessions = fetch_history(db_file=config.DATABASE_FILE, limit=50)
    return jsonify({'sessions': sessions})

if __name__ == '__main__':
    app.run(debug=True)
