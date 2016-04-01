import sys

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        a, b = map(int, test.split(","))
        print(a - (a // b * b))
    test_cases.close()
main()