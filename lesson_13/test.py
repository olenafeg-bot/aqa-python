import unittest
import logging
import os
# Припускаємо, що функція знаходиться у файлі login_system.py
from lesson_13.homework_10 import log_event

LOG_FILE = 'login_system.log'


class TestLogEvent(unittest.TestCase):

    # def setUp(self):
    # #     """
    # #     Налаштування перед кожним тестом.
    # #     1. Скидаємо конфігурацію кореневого логера, щоб basicConfig спрацював у функції.
    # #     2. Видаляємо файл логів для чистого старту.
    # #     """
    # #     # Скидання конфігурації логування
    #     root_logger = logging.getLogger()
    #     for handler in root_logger.handlers[:]:
    #         root_logger.removeHandler(handler)
    #
    #     # Очищення лог-файлу, якщо він був створений
    #     if os.path.exists(LOG_FILE):
    #         os.remove(LOG_FILE)
    #
    # def tearDown(self):
    #     """
    #     Очищення після кожного тесту: гарантує видалення лог-файлу.
    #     """
    #     if os.path.exists(LOG_FILE):
    #         os.remove(LOG_FILE)

    def test_log_event_success_logs_info(self):
        """Перевіряє, що статус 'success' логується на рівні INFO."""
        username = "olena"
        status = "success"
        expected_message = f"Login event - Username: {username}, Status: {status}"

        # assertLogs захоплює лог-записи для логера з ім'ям 'log_event'
        with self.assertLogs('log_event', level='INFO') as cm:
            log_event(username, status)

            # Перевірка, що було записано рівно одне повідомлення
            self.assertEqual(len(cm.output), 1)
            # Перевірка, що повідомлення містить очікуваний текст та рівень
            # cm.output[0] містить рядок у форматі 'РІВЕНЬ:ІМ'Я_ЛОГЕРА:ПОВІДОМЛЕННЯ'
            self.assertIn('INFO:log_event:', cm.output[0])
            self.assertIn(expected_message, cm.output[0])

    def test_log_event_expired_logs_warning(self):
        """Перевіряє, що статус 'expired' логується на рівні WARNING."""
        username = "petro"
        status = "expired"
        expected_message = f"Login event - Username: {username}, Status: {status}"

        with self.assertLogs('log_event', level='WARNING') as cm:
            log_event(username, status)

            self.assertEqual(len(cm.output), 1)
            self.assertIn('WARNING:log_event:', cm.output[0])
            self.assertIn(expected_message, cm.output[0])

    def test_log_event_failed_logs_error(self):
        """Перевіряє, що статус 'failed' логується на рівні ERROR."""
        username = "hacker"
        status = "failed"
        expected_message = f"Login event - Username: {username}, Status: {status}"

        with self.assertLogs('log_event', level='ERROR') as cm:
            log_event(username, status)

            self.assertEqual(len(cm.output), 1)
            self.assertIn('ERROR:log_event:', cm.output[0])
            self.assertIn(expected_message, cm.output[0])

    def test_log_event_unknown_status_logs_error(self):
        """
        Перевіряє, що будь-який невідомий статус логується на рівні ERROR
        (відповідно до блоку 'else').
        """
        username = "unknown_user"
        status = "unknown_status"
        expected_message = f"Login event - Username: {username}, Status: {status}"

        with self.assertLogs('log_event', level='ERROR') as cm:
            log_event(username, status)

            self.assertEqual(len(cm.output), 1)
            self.assertIn('ERROR:log_event:', cm.output[0])
            self.assertIn(expected_message, cm.output[0])

    def test_log_event_writes_to_file(self):
        """
        Додатковий тест для перевірки, чи дійсно створюється і записується лог-файл
        (як було запитано в попередній ітерації).
        """
        username = "file_check"
        status = "success"
        # Очікуваний підрядок (без timestamp)
        expected_substring = f" - Login event - Username: {username}, Status: {status}"

        log_event(username, status)

        self.assertTrue(os.path.exists(LOG_FILE), "Лог-файл має бути створено.")

        # Читаємо файл і перевіряємо вміст
        with open(LOG_FILE, 'r', encoding='utf-8') as f:
            log_content = f.read().strip()

        self.assertIn(expected_substring, log_content)


if __name__ == '__main__':
    unittest.main()
