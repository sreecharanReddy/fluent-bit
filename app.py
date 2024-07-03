import time
import logging
import traceback

# Configure logging
log_file = '/logs/app.log'  # Specify the path to the log file
logging.basicConfig(level=logging.INFO, 
                    format='[%(asctime)s] - [%(levelname)s] - [REAL-TIME-OFFERS] - [%(message)s]',
                    handlers=[
                        logging.FileHandler(log_file),
                        logging.StreamHandler()
                    ])

# Simple log messages
def log_messages():
    i = 1
    while True:
        logging.info(f"This is an info message - {i}")
        try:
            if i%2 == 0:
                logging.warning(f"This is an warning message - {i}")
            if i%5 == 0:
                k = 0/0
        except Exception as e:
            logging.error(f"This is an error message - {e}")

        time.sleep(5)
        i += 1

if __name__ == "__main__":
    log_messages()
