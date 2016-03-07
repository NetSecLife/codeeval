import sys

def main():
    test_cases = open(sys.argv[1], 'r')
    dict = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
            "six": 6, "seven": 7, "eight": 8, "nine": 9}
    for test in test_cases:
        list = test.split(";")
        result = ""
        for i in list:
            i = i.strip('\n')
            result += str(dict[i])
        print(str(result))
    test_cases.close()

main()