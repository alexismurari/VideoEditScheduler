import unittest

from schedule.publish import convert_time

class TestConvertTime(unittest.TestCase):
    def test_convert_time(self):
        """
        Check if the time is returned correctly
        """
        r = convert_time((2020,2,5),(20,0))
        self.assertEqual(r, "2020-02-05T20:00:00-05:00")

if __name__ == '__main__':
    unittest.main()