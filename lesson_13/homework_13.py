
import unittest
import os

from lesson_13.homework_10 import log_event


class TestLogEvent(unittest.TestCase):

    LOG_FILE = "login_system.log"


    def test_log_event_success(self):
        username = "olena"
        status = "success"

        log_event(username, status)


        with open(self.LOG_FILE, "r") as file:
            content = file.read()

        self.assertIn(f"Username: {username}", content)
        self.assertIn(f"Status: {status}", content)


    def test_log_event_unknown_status(self):
        username = "olena"
        status = "expired"

        log_event(username, status)

        with open(self.LOG_FILE, "r") as file:
            content = file.read()

        self.assertIn(f"Username: {username}", content)
        self.assertIn(f"Status: {status}", content)

    def test_log_event_error(self):
        username = "olena"
        status = "error"

        log_event(username, status)

        with open(self.LOG_FILE, "r") as file:
            content = file.read()

        self.assertIn(f"Username: {username}", content)
        self.assertIn(f"Status: {status}", content)

if __name__ == "__main__":
    unittest.main()
