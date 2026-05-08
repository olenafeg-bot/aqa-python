import logging

# Створення логера
custom_logger_file = logging.getLogger("custom_logger_file")

# #Налаштування рівня логування
custom_logger_file.setLevel(logging.DEBUG)
custom_logger_file.propagate = False
# Створення обробника для запису в файл
file_handler = logging.FileHandler('custom_logger_file.log')

# Налаштування рівня логування для обробника
file_handler.setLevel(logging.INFO)

# Створення форматера для обробника
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s %(filename)s:%(lineno)d')
file_handler.setFormatter(formatter)

# #Додавання обробника до логера
custom_logger_file.addHandler(file_handler)

# Логування подій
custom_logger_file.debug('Message level DEBUG')
custom_logger_file.info('Message level INFO')
custom_logger_file.warning('Message level WARNING')
custom_logger_file.error('Message level ERROR')
custom_logger_file.critical('Message level CRITICAL')