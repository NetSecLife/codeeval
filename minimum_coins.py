import sys

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        count = 0
        test = int(test)
        while test != 0:
            if test >= 5:
                test -= 5
                count += 1
            elif test >= 3 and test < 5:
                test -= 3
                count += 1
            elif test > 0 and test < 3:
                test -= 1
                count += 1
        print(count)
    test_cases.close()

main()