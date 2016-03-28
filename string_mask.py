import sys

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        w1,w2 = test.strip().split()
        res = []
        for i in range(len(w1)):
            if w2[i] == '1':
                a = w1[i].upper()
                res.append(a)
            elif w2[i] == '0':
                a = w1[i].lower()
                res.append(a)
        print(''.join(res))
    test_cases.close()

main()