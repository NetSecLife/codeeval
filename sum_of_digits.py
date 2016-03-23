import sys

def main():
    test_cases = open(sys.argv[1], 'r')
    for i in test_cases:
        l = list(i.strip('\n'))
        res = 0
        for z in l:
            z = int(z)
            res += z
        print(res)
    test_cases.close()

main()