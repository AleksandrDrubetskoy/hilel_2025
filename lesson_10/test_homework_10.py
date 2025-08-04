import unittest
from homework_10 import log_event

logger_file = 'login_system.log'


def read_last_log_line():
    with open(logger_file, mode="r") as f:
        log_text = f.read()
        return log_text.split("\n")[-2]


class MyTestLogger(unittest.TestCase):

    # status checking
    def test_success_status_log_event(self):
        username_expected = 'Sasha'
        status_expected = 'success'
        log_event(username_expected, status_expected)
        expected_log_event = [username_expected, status_expected]
        username_actual = read_last_log_line().split()[-3][:-1]
        status_actual = read_last_log_line().split()[-1]
        actual_log_event = [username_actual, status_actual]
        self.assertEqual(expected_log_event, actual_log_event)

    def test_expired_status_log_event(self):
        username_expected = 'Sasha'
        status_expected = 'expired'
        log_event(username_expected, status_expected)
        expected_log_event = [username_expected, status_expected]
        username_actual = read_last_log_line().split()[-3][:-1]
        status_actual = read_last_log_line().split()[-1]
        actual_log_event = [username_actual, status_actual]
        self.assertEqual(expected_log_event, actual_log_event)

    def test_failed_status_log_event(self):
        username_expected = 'Sasha'
        status_expected = 'Sasha'
        log_event(username_expected, status_expected)
        expected_log_event = [username_expected, status_expected]
        username_actual = read_last_log_line().split()[-3][:-1]
        status_actual = read_last_log_line().split()[-1]
        actual_log_event = [username_actual, status_actual]
        self.assertEqual(expected_log_event, actual_log_event)

    # level checking
    def test_success_level_log_event(self):
        username_expected = 'Sasha'
        status_expected = 'success'
        log_event(username_expected, status_expected)
        expected_level = 'INFO'
        actual_level = read_last_log_line().split()[3]
        self.assertEqual(expected_level, actual_level)

    def test_expired_level_log_event(self):
        username_expected = 'Sasha'
        status_expected = 'expired'
        log_event(username_expected, status_expected)
        expected_level = 'WARNING'
        actual_level = read_last_log_line().split()[3]
        self.assertEqual(expected_level, actual_level)

    def test_failed_level_log_event(self):
        username_expected = 'Sasha'
        status_expected = 'Sasha'
        log_event(username_expected, status_expected)
        expected_level = 'ERROR'
        actual_level = read_last_log_line().split()[3]
        self.assertEqual(expected_level, actual_level)
