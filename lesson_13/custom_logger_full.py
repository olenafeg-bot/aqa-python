import logging

# Створення логера
custom_logger_full = logging.getLogger("custom_logger_full")

# Налаштування рівня логування
custom_logger_full.setLevel(logging.DEBUG)

 # Створення обробника для виводу в stdout (консоль)
console_handler = logging.StreamHandler()

# Створення обробника для запису в файл
file_handler = logging.FileHandler('custom_logger_full.log')

# Налаштування рівня логування для обробників
console_handler.setLevel(logging.WARNING)
file_handler.setLevel(logging.DEBUG)

# Створення форматера для обробників
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s %(filename)s:%(lineno)d')
console_formatter = logging.Formatter('%(levelname)s - %(message)s')
# Налаштування форматера для обробників
console_handler.setFormatter(console_formatter)

file_handler.setFormatter(file_formatter)

 # Додавання обробників до логера
custom_logger_full.addHandler(console_handler)
custom_logger_full.addHandler(file_handler)

 # Логування подій
custom_logger_full.debug('Message level DEBUG')
custom_logger_full.info('Message level INFO')
custom_logger_full.warning('Message level WARNING')
custom_logger_full.error('Message level ERROR')
custom_logger_full.critical('Message level CRITICAL')


