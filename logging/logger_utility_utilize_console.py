"""
Example:
Using logger utility with file logging - console only
"""

from logger_utility import get_logger

# Create logger object (logfile anme and file_mode not provided hence console)
logger = get_logger("app")

# Log messages
logger.debug("Debug message from app1")
logger.info("Info message from app1")
logger.warning("Warning message from app1")
logger.error("Error message from app1")
logger.critical("Critical message from app1")