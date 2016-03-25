import sys

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        l1,l2 = test.strip().split('|')
        l1 = l1.strip().split(' ')
        l2 = l2.strip().split(' ')
        res = []
        for i in range(len(l1)):
            z = int(l1[i]) * int(l2[i])
            res.append(str(z))
        print(' '.join(res))
    test_cases.close()
main()
