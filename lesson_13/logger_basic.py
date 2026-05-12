import logging

# logging.basicConfig(filename="example.log", level=logging.INFO, encoding="utf-8",format="%(asctime)s - %(name)s - %(levelname)s - %(message)s %(filename)s:%(lineno)d")
#
# logging.debug('Це повідомлення рівня DEBUG')
# logging.info('Це повідомлення рівня INFO')
# logging.warning('Це повідомлення рівня WARNING')
# logging.error('Це повідомлення рівня ERROR')
# logging.critical('Це повідомлення рівня CRITICAL')

# Створення конфігурації
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.StreamHandler(),  # Виведення в консоль
                        logging.FileHandler('example.log')  # Запис у файл
                    ])

# Використання логера
logger = logging.getLogger(__name__)

logger.debug('Message level DEBUG')
logger.info('Message level INFO')