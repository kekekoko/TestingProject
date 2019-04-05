import math


class NumberIncreaser:
    # 375 [Easy}

    def increaseNumber(self, inputNumber):
        # get number of digits
        bla = 10
        blub = 10
        while inputNumber >= bla:
            bla = bla * blub

        numberOfDigits = int(math.log10(bla))

        outputNumber = inputNumber

        exponent = 0
        while exponent < numberOfDigits:
            currentDigit = (outputNumber % (10 ** (exponent + 1))) // (10 ** exponent)
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
