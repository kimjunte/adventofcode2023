def modifyLinetoNumbers(originol_string):
    numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    

    dict_num = {
        "one": "o1e",
        "two": "t2o",
        "three": "t3e",
        "four": "f4r",
        "five": "f5e",
        "six": "s6x",
        "seven": "s7n",
        "eight": "e8t",
        "nine": "n9e",
    }


    originol_string = originol_string.lower()

    for number in numbers:
            originol_string = originol_string.replace(number, dict_num[number])
    return originol_string



def getFirstNumber(line):
    numberAsLetters = ["one"]
    number = None
    for char in line:
        if char.isdigit():
            return int(char)

def getLastNumber(string):
    return getFirstNumber(string[::-1])

def getCalibrationValue(string):
    modifiedNumber = modifyLinetoNumbers(string)
    firstnumber = getFirstNumber(modifiedNumber)
    secondnumber = getLastNumber(modifiedNumber)
    calibrationValue = str(firstnumber) + str(secondnumber)
    return int(calibrationValue)

def validate(a, b):
    assert a == b, "Test failed"
    return a == b

def test():
    # Problem 1
    validate(getFirstNumber("1abc2"), 1)
    validate(getFirstNumber("pqr3stu8vwx"), 3)
    validate(getFirstNumber("a1b2c3d4e5f"), 1)
    validate(getFirstNumber("treb7uchet"), 7)

    validate(getLastNumber("1abc2"), 2)
    validate(getLastNumber("pqr3stu8vwx"), 8)
    validate(getLastNumber("a1b2c3d4e5f"), 5)
    validate(getLastNumber("treb7uchet"), 7)

    validate(getCalibrationValue("1abc2"), 12)
    validate(getCalibrationValue("pqr3stu8vwx"), 38)
    validate(getCalibrationValue("a1b2c3d4e5f"), 15)
    validate(getCalibrationValue("treb7uchet"), 77)

    # Problem 2
    validate(getCalibrationValue("two1nine"), 29)
    validate(getCalibrationValue("eightwothree"), 83)
    validate(getCalibrationValue("abcone2threexyz"), 13)
    validate(getCalibrationValue("xtwone3four"), 24)
    validate(getCalibrationValue("4nineeightseven2"), 42)
    validate(getCalibrationValue("zoneight234"), 14)
    validate(getCalibrationValue("7pqrstsixteen"), 76)


def main():
    calibrationValue = 0
    with open("input.txt", "r") as magicalElfFile:
        for line in magicalElfFile.readlines():
            calibrationValue += getCalibrationValue(line)
        print(calibrationValue)

if __name__ == "__main__":
    test()
    main()
