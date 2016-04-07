import sys

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        l1, l2 = test.strip().split(':')
        l1 = l1.split()
        l2 = l2.split(',')
        l2 = list(map(lambda x: x.strip(), l2))
        for i in l2:
            p1,p2 = i.split('-')
            p1 = int(p1)
            p2 = int(p2)
            lp1 = l1[p1]
            lp2 = l1[p2]
            l1[p1] = lp2
            l1[p2] = lp1
        print(' '.join(l1))
    test_cases.close()

main()