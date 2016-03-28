import sys

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        test_string = test.strip().split()
        index = test_string[-1:]
        index = int(index[0])
        string = ''.join(test_string[:-1])
        if index > len(string):
            continue
        elif index <= len(string):
            print(string[-index])
    test_cases.close()

main()