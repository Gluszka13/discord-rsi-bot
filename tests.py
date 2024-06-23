import unittest
from bot import fetch_klines, calculate_rsi, PERIOD

class TestBotFunctions(unittest.TestCase):
    def test_fetch_klines(self):
        klines = fetch_klines()
        self.assertIsInstance(klines, list)
        self.assertEqual(len(klines), PERIOD)

    def test_calculate_rsi(self):
        # Example data, 14 klines, (timestamp, open, high, low, close, volume, quote_volume)
        example_data = [
            ['1719158400000', '131.59', '131.91', '131.21', '131.74', '6831.076', '898775.2442'],
            ['1719154800000', '132.24', '132.68', '131.42', '131.59', '27353.218', '3612465.96337'],
            ['1719151200000', '133.56', '133.65', '132', '132.24', '32717.118', '4341696.17199'],
            ['1719147600000', '133.93', '134.29', '133.46', '133.56', '14938.873', '1999344.22051'],
            ['1719144000000', '134.04', '134.38', '133.89', '133.93', '13324.658', '1786897.59415'],
            ['1719140400000', '133.87', '134.27', '133.45', '134.04', '21333.93', '2854630.49151'],
            ['1719136800000', '134.69', '134.76', '133.71', '133.87', '16309.553', '2188735.55635'],
            ['1719133200000', '134.54', '134.83', '134.2', '134.69', '10974.817', '1476347.62822'],
            ['1719129600000', '134.72', '134.77', '134.46', '134.54', '6956.373', '936193.41548'],
            ['1719126000000', '134.41', '134.79', '134.39', '134.72', '8957.634', '1205960.11535'],
            ['1719122400000', '134.43', '134.69', '134.32', '134.41', '7872.588', '1058699.48077'],
            ['1719118800000', '134.58', '134.86', '134.19', '134.43', '8355.51', '1123778.22523'],
            ['1719115200000', '134.78', '135.04', '134.56', '134.58', '10566.302', '1424494.20559'],
            ['1719111600000', '134.8', '135.12', '134.43', '134.78', '11973.113', '1613137.38713']
        ]
        rsi = calculate_rsi(example_data)
        self.assertIsInstance(rsi, float)
        self.assertAlmostEqual(rsi, 80.92747987946166)

if __name__ == '__main__':
    unittest.main()
