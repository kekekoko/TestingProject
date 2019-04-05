import numpy as np

class RevisedJulianCalendar:
    def getNumberOfLeapDays(self, firstYear, secondYear):
        if (firstYear > secondYear):
            raise ValueError('First year must be bigger than second year!')
        if firstYear == secondYear:
            return 0

        difference = secondYear - firstYear
        yearsDividableBy4 = self.getYearsDividableBy(4, firstYear, difference)

        lcM4_100 = np.lcm(4, 100)
        yearsDividableBy4And100 = self.getYearsDividableBy(lcM4_100, firstYear, difference)

        exceptionExceptionYears = self.getYearsWithWeirdRemainders(firstYear, difference)

        totalYears = yearsDividableBy4 - (yearsDividableBy4And100 - exceptionExceptionYears)

        return totalYears

    def getYearsWithWeirdRemainders(self, firstYear, difference):
        yearsDividableBy900withWeirdRemainders = (difference // 900) * 2
        rd900 = difference % 900
        rf900 = firstYear % 900
        if rf900 == 200 or rf900 == 600:
            yearsDividableBy900withWeirdRemainders += 1
        addedRemainders = rf900 + rd900
        if rf900 < 200 and addedRemainders > 200:
            yearsDividableBy900withWeirdRemainders += 1
        if rf900 < 600 and addedRemainders > 600:
            yearsDividableBy900withWeirdRemainders += 1
        if rf900 > 200 and rf900 <= 600 and addedRemainders > 900 and addedRemainders % 900 > 200:
            yearsDividableBy900withWeirdRemainders += 1
        return yearsDividableBy900withWeirdRemainders


    def getYearsDividableBy(self, number, firstYear, difference):
        yearsDividableBy4 = difference // number
        rd4 = difference % number
        rf4 = firstYear % number
        if (rf4 == 0 and rd4 != 0) or (rd4 != 0 and rd4 + rf4 > number):
            yearsDividableBy4 += 1

        return yearsDividableBy4

