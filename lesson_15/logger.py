
import logging

# налаштовуємо один раз
logging.basicConfig(
    filename='json_fehetsyn.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)'
)

logger = logging.getLogger("json_logger")


def log_event(file_name: str, status: str):
    log_message = f"File: {file_name}, Status: {status}"

    if status == "OK":
        logger.info(log_message)
    else:
        logger.error(log_message)
