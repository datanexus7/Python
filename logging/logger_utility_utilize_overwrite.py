"""
app1.py

Example:
Using logger utility with file logging - overwrite
"""

from logger_utility import get_logger

# Create logger object with overwrite (file_mode = "w")
logger = get_logger("app", "logs/app_overwrite.log", file_mode="w")

# Log messages
logger.debug("Debug message from app1")
logger.info("Info message from app1")
logger.warning("Warning message from app1")
logger.error("Error message from app1")
logger.critical("Critical message from app1")