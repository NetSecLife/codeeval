import sys

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        last = " "
        res = []
        for i in test:
            if i.lower() == last:
                pass
            else:
                res += i
                last = i
        print(''.join(res))
    test_cases.close()

main()