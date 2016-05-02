import sys
import operator

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        l1 = test.strip().split(';')
        l2 = []
        for i in l1:
            i = i.strip()
            l2.append(i.split(','))
        l2 = l2[:-1]
        l3 = sorted(l2, key=operator.itemgetter(1))
        l4 = []
        for i in range(0,len(l3)):
            if l4 == []:
                l4.append(l3[i][1])
            else:
                l4.append(str(int(l3[i][1]) - int(l3[i-1][1])))
        print(','.join(l4))

main()