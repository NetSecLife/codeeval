#this is a very haskish way of doing it abusing the constraints

import sys

def main():
    primes = [3,7,31,127,2047]
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        test = int(test.strip())
        res = []
        for i in primes:
            if test > i:
                res.append(str(i))
            else:
                break
        print(', '.join(res))
    test_cases.close()

main()