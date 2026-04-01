import json
import datetime
import os

DATA_FILE = 'fruits.json'
LOG_FILE = 'transactions.log'

def load_data():
    """Business Logic: Load fruit stock from JSON file into a dictionary."""
    if not os.path.exists(DATA_FILE):
        return {}
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError):
        log_transaction("Error: Failed to read data file. Starting fresh.")
        return {}

def save_data(data):
    """Business Logic: Save dictionary data back to the JSON file."""
    try:
        with open(DATA_FILE, 'w') as file:
            json.dump(data, file, indent=4)
    except IOError as e:
        log_transaction(f"Critical Error saving data: {e}")

def log_transaction(message):
    """Business Logic: Append transaction details to the log file."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {message}\n"
    
    with open(LOG_FILE, 'a') as file:
        file.write(log_entry)