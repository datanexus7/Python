"""
logger_utility.py

Reusable logging utility module.
Supports:
- Console logging
- File logging
- Append / Overwrite modes
"""

import logging
import os


def get_logger(script_name, log_file=None, file_mode="a"):
    """
    Create and return a configured logger.

    Parameters:
    -----------
    script_name : str
        Name of the calling Python script

    log_file : str, optional
        File path to store logs
        If not provided → logs only on console

    file_mode : str, default="a"
        Log file write mode:
        - "a" = append logs (default)
        - "w" = overwrite logs each run

    Returns:
    --------
    logger object
    """

    try:

        # ---------------------------------------------------------
        # STEP 1: Create logger object
        # ---------------------------------------------------------
        logger = logging.getLogger(script_name)
        logger.setLevel(logging.DEBUG)

        # ---------------------------------------------------------
        # STEP 2: Avoid duplicate logs
        # ---------------------------------------------------------
        if logger.hasHandlers():
            logger.handlers.clear()

        # ---------------------------------------------------------
        # STEP 3: Create formatter
        # ---------------------------------------------------------
        formatter = logging.Formatter(
            '%(asctime)s | %(levelname)s | '
            '%(filename)s:%(lineno)d | %(message)s',
            datefmt='%d-%b-%Y %I:%M:%S %p'
        )

        # ---------------------------------------------------------
        # STEP 4: Console handler (always enabled)
        # ---------------------------------------------------------
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        # ---------------------------------------------------------
        # STEP 5: File handler (optional)
        # ---------------------------------------------------------
        if log_file:

            # STEP 5.1: Create directory if not exists
            log_dir = os.path.dirname(log_file)

            if log_dir and not os.path.exists(log_dir):
                os.makedirs(log_dir)

            # STEP 5.2: Validate file_mode
            if file_mode not in ["a", "w"]:
                raise ValueError("file_mode must be 'a' (append) or 'w' (overwrite)")

            # STEP 5.3: Create file handler with mode
            file_handler = logging.FileHandler(log_file, mode=file_mode)
            file_handler.setFormatter(formatter)

            logger.addHandler(file_handler)

            # STEP 5.4: Print status
            mode_text = "APPEND" if file_mode == "a" else "OVERWRITE"

            print(f"Logging enabled on console and file: {log_file} ({mode_text})")

        else:

            # Console only mode
            print("Logging enabled on console only")

        # ---------------------------------------------------------
        # STEP 6: Return logger
        # ---------------------------------------------------------
        return logger

    except Exception as error:

        # ---------------------------------------------------------
        # ERROR HANDLING
        # ---------------------------------------------------------
        print("Error while creating logger")
        print(f"Exception Details: {error}")

        raise
