import logging
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILEPATH = os.path.join(BASE_DIR, "app.log")


def setup_logger(log_filepath: str = LOG_FILEPATH) -> logging.Logger:
    """Configure a logger that writes all levels to both console and a log file."""
    logger = logging.getLogger("AppLogger")
    logger.setLevel(logging.DEBUG)
    logger.propagate = False

    # Clear existing handlers to prevent duplicate log entries on repeated calls
    if logger.hasHandlers():
        logger.handlers.clear()

    # Create console and file handlers
    console_handler = logging.StreamHandler()
    file_handler = logging.FileHandler(log_filepath, mode="w", encoding="utf-8")

    # Set severity threshold for both handlers
    console_handler.setLevel(logging.DEBUG)
    file_handler.setLevel(logging.DEBUG)

    # Create formatter and attach it to both handlers
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # Attach handlers to the logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    return logger


def main() -> None:
    logger = setup_logger(LOG_FILEPATH)

    # Demonstrate all 5 standard logging severity levels
    logger.debug("DEBUG: Initializing configuration parameters.")
    logger.info("INFO: Application workflow started successfully.")
    logger.warning("WARNING: Disk usage has reached 80% capacity.")
    logger.error("ERROR: Failed to connect to secondary backup server.")
    logger.critical("CRITICAL: Primary database connection lost; initiating failover.")

    # Demonstrate lazy variable formatting
    username = "sanskar"
    attempt_count = 3
    logger.info("User '%s' completed operation after %d attempts.", username, attempt_count)

    # Demonstrate capturing a full stack trace with logger.exception()
    donuts = 5
    guests = 0
    try:
        _ = donuts / guests
    except ZeroDivisionError:
        logger.exception("Calculation error while dividing %d donuts among %d guests.", donuts, guests)

    # Flush and verify file output
    for handler in logger.handlers:
        handler.flush()
    print(f"\nLogs successfully recorded to '{LOG_FILEPATH}'.")


if __name__ == "__main__":
    main()