from unittest import TestCase
from DailyProgrammer.Easy.PrintNewNumber.NumberIncreaser import NumberIncreaser


class TestNumberIncreaser(TestCase):

    def setUp(self):
        self.increaser = NumberIncreaser()

    def assertIncreaseNumberWorks(self, testNumber, expectedOutput):
        actualOutput = self.increaser.increaseNumber(testNumber)
        self.assertEqual(expectedOutput, actualOutput,
                         '{} not working, expected {} but was {}'.format(testNumber, expectedOutput, actualOutput))

    def test_2(self):
        self.assertIncreaseNumberWorks(2, 3)

    def test_9(self):
        self.assertIncreaseNumberWorks(9, 10)

    def test_11(self):
        self.assertIncreaseNumberWorks(11, 22)

    def test_19(self):
        self.assertIncreaseNumberWorks(19, 210)

    def test_99(self):
        self.assertIncreaseNumberWorks(99, 1010)

    def test_293(self):
        self.assertIncreaseNumberWorks(293, 3104)

    def test_999(self):
        self.assertIncreaseNumberWorks(999, 101010)

    def test_679429(self):
        self.assertIncreaseNumberWorks(679429, 78105310)
