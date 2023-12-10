
def validate(a, b):
    assert a == b, "Test failed"
    return a == b

def test():
    # Problem 2

def main():
    calibrationValue = 0
    with open("input.txt", "r") as magicalElfFile:
        for line in magicalElfFile.readlines():
            calibrationValue += getCalibrationValue(line)
        print(calibrationValue)

if __name__ == "__main__":
    test()
    main()
