import sys

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        res = []
        last = 0
        test = test.strip()
        for i in test:
            if i.isalpha():
                res.append(i.lower())
                last = 1
            elif last == 1:
                res.append(' ')
                last = 0
        res = ''.join(res)
        print(res.strip())
    test_cases.close()

main()