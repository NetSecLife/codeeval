import sys
def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        print(test.split()[-2])
    test_cases.close()
main()