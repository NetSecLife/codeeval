import sys

def main():
    with open(sys.argv[1], 'r') as test_cases:
        result = 0
        for test in test_cases:
            test = int(test)
            result += test
        print(result)

main()