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
