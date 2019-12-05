import unittest

from leap_year import LeapYear


class TestLeapYear(unittest.TestCase):

    def test2000(self):
        leapYear = LeapYear(2000)
        print(leapYear.answer())

    def test1900(self):
        leapYear = LeapYear(1900)
        print(leapYear.answer())

    def test2020(self):
        leapYear = LeapYear(2020)
        print(leapYear.answer())

    if __name__ == '__main__':
        unittest.main()
