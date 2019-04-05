from unittest import TestCase
from DailyProgrammer.Easy.RevisedJulianCalendar import RevisedJulianCalendar


class TestRevisedJulianCalendar(TestCase):

    def setUp(self):
        self.calendar = RevisedJulianCalendar.RevisedJulianCalendar()

    def checkCorrectLeapDays(self, fY, sY, expectedResult):
        result = self.calendar.getNumberOfLeapDays(fY, sY)
        self.assertEqual(expectedResult, result)

    def test_getNumberOfLeapDays_2016_2017(self):
        self.checkCorrectLeapDays(2016, 2017, 1)

    def test_getNumberOfLeapDays_2019_2020(self):
        self.checkCorrectLeapDays(2019, 2020, 0)

    def test_getNumberOfLeapDays_1900_1901(self):
        self.checkCorrectLeapDays(1900, 1901, 0)

    def test_getNumberOfLeapDays_2000_2001(self):
        self.checkCorrectLeapDays(2000, 2001, 1)

    def test_getNumberOfLeapDays_2800_2801(self):
        self.checkCorrectLeapDays(2800, 2801, 0)

    def test_getNumberOfLeapDays_123456_123456(self):
        self.checkCorrectLeapDays(123456, 123456, 0)

    def test_getNumberOfLeapDays_1234_5678(self):
        self.checkCorrectLeapDays(1234, 5678, 1077)

    def test_getNumberOfLeapDays_123456_7891011(self):
        self.checkCorrectLeapDays(123456, 7891011, 1881475)

    def test_getNumberOfLeapDays_123456789101112_1314151617181920(self):
        self.checkCorrectLeapDays(123456789101112, 1314151617181920, 288412747246240)

