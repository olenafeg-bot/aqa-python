import logging

# Створення логера
custom_logger_console = logging.getLogger("custom_logger_file")

# #Налаштування рівня логування
custom_logger_console.setLevel(logging.DEBUG)
custom_logger_console.propagate = False
# Створення обробника для запису в файл
console_handler = logging.StreamHandler()

# Налаштування рівня логування для обробника
console_handler.setLevel(logging.WARNING)

# Створення форматера для обробника
formatter = logging.Formatter('%(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

# #Додавання обробника до логера
custom_logger_console.addHandler(console_handler)

# Логування подій
custom_logger_console.debug('Message level DEBUG')
custom_logger_console.info('Message level INFO')
custom_logger_console.warning('Message level WARNING')
custom_logger_console.error('Message level ERROR')
custom_logger_console.critical('Message level CRITICAL')