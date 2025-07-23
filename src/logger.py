import logging
import os
from datetime import datetime

# 1. Generate timestamped filename
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# 2. Create a 'logs' directory (just the folder, not including the file)
logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)

# 3. Build full path to the log file inside that directory
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# 4. Configure logging to write into that file
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


