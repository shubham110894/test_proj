from loguru import logger
import os
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H_%M_%S")
logger.add(os.path.join(os.path.dirname(__file__), f'../reports/logs/automation_logs_{current_time}.log'))