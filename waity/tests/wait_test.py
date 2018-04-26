import time
import pytest
from waity import wait


def get_true():
    return True


def get_false():
    return False


def get_sleep():
    time.sleep(3)
    return True


class TestWait:
    def test_true_condition(self):
        start = time.time()
        wait.condition(lambda: get_true())
        end = time.time()
        assert round(end) == round(start)

    def test_false_condition(self):
        start = time.time()
        with pytest.raises(TimeoutError):
            wait.condition(lambda: get_false())
        end = time.time()
        assert round(end) == round(start + 10)

    def test_sleep_condition(self):
        start = time.time()
        wait.condition(lambda: get_sleep())
        end = time.time()
        assert round(end) == round(start + 3)
