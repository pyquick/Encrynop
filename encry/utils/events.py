import threading
import signal
import sys
import time
from .loin import * # Import LogManager from log module

shutdown_event = threading.Event()
 # Create LogManager instance

# Define signal handler function
def _signal_handler(signum, frame):
    time.sleep(0.2)
    init_logger = LogManager("_signal_handler", "INFO")
    init_logger.info("Ctrl+C (SIGINT) detected. Setting global shutdown event...")
    shutdown_event.set()
    init_logger.info("Global shutdown event has been set.")
    threading.Thread(target=time.sleep(0.8)).start()
    init_logger.info("Exiting...")
    try:
        sys.exit(0)
    except SystemExit:
        pass
    #exit(0)


signal.signal(signal.SIGINT, _signal_handler)
