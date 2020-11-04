import time
import unittest

from src.davil.strings import nums_from_string
from src.davil.timings import Timings


class TestTimingsContextManager(unittest.TestCase):

    def test(self):
        timer = Timings()
        with timer('a'):
            time.sleep(1)

        with timer('a'):
            time.sleep(1)

        with timer('b'):
            time.sleep(1)

        assert round(timer['a']) == 2.0
        assert round(timer['b']) == 1.0

        p = timer.percentages(ret=True)
        times = nums_from_string(p)
        times = [int(x[0:2]) for x in times]
        assert times[1] == 66
        assert times[3] == 33


if __name__ == '__main__':
    unittest.main()
