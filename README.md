# Toyota 5A-FE OBD-I Professional Scanner

**WORK IN PROGRESS BY: H. Pandit**

A Flask-based diagnostic tool for Toyota’s 5A-FE OBD-I ECU, supporting simulation and real hardware, with data-logging and live streaming.

## Features

- **Scan** & clear codes (simulation or real serial port)
- **Live data** dashboard (RPM, coolant temp, etc.)
- **Session history** (SQLite)
- **Modular** code structure for easy extension
- Configurable via `config.py`

## Quickstart

```bash
git clone https://github.com/yourusername/toyota-5a-obd-scanner.git
cd toyota-5a-obd-scanner
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
export FLASK_APP=app.py
flask run

## Roadmap & Enhancements

### 1. Hardware Integration
- **ISO 9141-2 / K-Line Protocol**  
  Add `src/obd_protocol.py` using `python-OBD` to speak Toyota’s 5A-FE ECU language.
- **ELM327 & Bluetooth/Wi-Fi Support**  
  Create a `BluetoothAdapter` class in `src/adapters.py` to wrap PySerial/PyBluez for KiWi3-style dongles.

### 2. Diagnostic Depth
- **Expanded PID Coverage**  
  Import Toyota-specific PIDs (Engine RPM, Coolant Temp, Throttle Position) from a `data/toyota_pids.json`.
- **Bidirectional Controls**  
  Module `src/actuators.py` for relay-trigger tests (e.g., fuel pump, idle valve).

### 3. UI/UX Upgrades
- **Live Data Graphing**  
  Integrate Chart.js in `templates/index.html` to plot real-time streams.
- **Error Prioritization & Tutorials**  
  Enhance `static/js/main.js` to group codes by severity and link out to repair articles.

### 4. Community & Validation
- **Forum Feedback**  
  Draft a “How to Test” guide in `docs/validation.md` for Toyota-owner communities.
- **Adapter Recommendations**  
  List sub-$50 options (Launch CR529, KiWi3) on the front page.
