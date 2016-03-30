import sys

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        lst = test.strip().split(' ')
        lst = list(map(float, lst))
        lst = sorted(lst)
        res = []
        for i in lst:
            res.append("%.3f" % i)
        lst = list(map(str, res))
        print(' '.join(lst))
    test_cases.close()
    
main()