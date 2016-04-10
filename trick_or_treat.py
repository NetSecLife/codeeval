import sys
import math

def mknum(i):
    string = []
    for s in i:
        if s.isdigit():
            string.append(s)
    return ''.join(string)

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        v,z,w,h = test.strip().split(',')
        v = int(mknum(v))
        z = int(mknum(z))
        w = int(mknum(w))
        h = int(mknum(h))
        k = v + z + w
        r = ((((v * 3) +  (z * 4) + (w * 5)) * h) / k)
        print(math.floor(r))
    test_cases.close()
main()