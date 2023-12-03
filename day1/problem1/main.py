def getFirstNumber(line):
    number = None
    for char in line:
        if char.isdigit():
            return int(char)

def getLastNumber(string):
    return getFirstNumber(string[::-1])

def getCalibrationValue(string):
    firstnumber = getFirstNumber(string)
    secondnumber = getLastNumber(string)
    calibrationValue = str(firstnumber) + str(secondnumber)
    return int(calibrationValue)

def validate(a, b):
    assert a == b, "Test failed"
    return a == b

def test():
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


def main():
    calibrationValue = 0
    with open("input.txt", "r") as magicalElfFile:
        for line in magicalElfFile.readlines():
            calibrationValue += getCalibrationValue(line)
        print(calibrationValue)

if __name__ == "__main__":
    test()
    main()
