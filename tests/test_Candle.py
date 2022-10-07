import unittest
import sys,os
sys.path.append(f".{os.sep}/production")
import Candle as c


class TestCandle(unittest.TestCase):
    def setUp(self):
        self.c1 = c.Candle("SPY",100, 102, 98,101)

    def test_candle_open(self):
        self.assertEqual(self.c1.get_open(), 100)

    def test_candle_high(self):
            self.assertEqual(self.c1.get_high(), 102)

    def test_candle_low(self):
        self.assertEqual(self.c1.get_low(), 98)

    def test_candle_close(self):
        self.assertEqual(self.c1.get_close(), 101)

if __name__ == '__main__':
    unittest.main()
