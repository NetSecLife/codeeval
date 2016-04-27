import sys
import math

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        dd = float(test)
        d, m = test.strip().split('.')
        m = int((dd - int(d)) * 60)
        s = (dd - int(d) - m / 60) *3600
        s = math.floor(s)
        print('%i.%02d\'%02d\"' % (int(d),m, s))
    test_cases.close()
main()