

import logging
import os
from datetime import datetime

# Generate log file name
LOG_FILE = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"  # Example: 11_02_2024_00_22_49.log

# Define the directory for logs
logs_directory = os.path.join(os.getcwd(), "logs" ,LOG_FILE)  # Directory: C:\mlproject\logs

# Create the logs directory if it doesn't exist
os.makedirs(logs_directory, exist_ok=True)

# Full log file path
LOG_FILE_PATH = os.path.join(logs_directory, LOG_FILE)  # File: C:\mlproject\logs\11_02_2024_00_22_49.log

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# Example logging
logging.info("Logging has been configured!")
