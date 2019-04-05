import math

def increaseNumber(inputNumber):
    # get number of digits
    bla = 10
    blub = 10
    while inputNumber >= bla:
        bla = bla * blub

    numberOfDigits = int(math.log10(bla))

    outputNumber = inputNumber

    exponent = 0
    while exponent < numberOfDigits:
        currentDigit = (outputNumber % (10 ** (exponent + 1))) // (10**exponent)
        if currentDigit != 9:
            outputNumber += 10 ** exponent
        else:
            r = (outputNumber // (10 ** (exponent + 1)))
            digitsBefore = r * (10 ** (exponent + 1))
            if (exponent == 0):
                digitsAfter = 0
            else:
                digitsAfter = (outputNumber % (10 ** (exponent)))
            shiftedLeftDigitsBefore = digitsBefore * 10
            outputNumber = shiftedLeftDigitsBefore + 10 ** (exponent + 1) + digitsAfter
            exponent += 1
            numberOfDigits += 1

        exponent += 1

    return outputNumber


def unitTestIncreaseNumber(testNumber, expectedResult):
    actualResult = increaseNumber(testNumber)
    if actualResult != expectedResult:
        raise Exception('{} not working, expected {} but was {}'.format(testNumber, expectedResult, actualResult))


unitTestIncreaseNumber(2, 3)
unitTestIncreaseNumber(9, 10)
unitTestIncreaseNumber(11, 22)
unitTestIncreaseNumber(19, 210)
unitTestIncreaseNumber(99, 1010)
unitTestIncreaseNumber(293, 3104)
unitTestIncreaseNumber(999, 101010)
unitTestIncreaseNumber(679429, 78105310)


print("Hello cats")
inputNumber = int(input("Please enter the starting number: "))

result = increaseNumber(inputNumber)

print(result)


