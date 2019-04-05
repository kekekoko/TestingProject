class NumberIncreaser:
    # 375 [Easy}

    def increaseNumber(self, number):

        numberOfDigits = self.getNumberOfDigits(number)

        currentDigit = 0
        while currentDigit < numberOfDigits:
            currentDigitValue = (number % (10 ** (currentDigit + 1))) // (10 ** currentDigit)
            if currentDigitValue != 9:
                number += 10 ** currentDigit
            else:
                r = (number // (10 ** (currentDigit + 1)))
                digitsBefore = r * (10 ** (currentDigit + 1))
                if currentDigit == 0:
                    digitsAfter = 0
                else:
                    digitsAfter = (number % (10 ** currentDigit))
                shiftedLeftDigitsBefore = digitsBefore * 10
                number = shiftedLeftDigitsBefore + 10 ** (currentDigit + 1) + digitsAfter
                currentDigit += 1
                numberOfDigits += 1

            currentDigit += 1

        return number

    def getNumberOfDigits(self, number):
        numberOfDigits = 1;
        comparisonNumber = 10
        while number >= comparisonNumber:
            comparisonNumber = comparisonNumber * 10
            numberOfDigits += 1

        return numberOfDigits


if __name__ == '__main__':
    print("Hello cats")
    while True:
        print("Please enter the starting number. Type 'exit' to exit.")
        inNum = input("Number: ")
        if inNum == 'exit':
            break
        inputNumber = int(inNum)
        increaser = NumberIncreaser()
        result = increaser.increaseNumber(inputNumber)
        print(result)
