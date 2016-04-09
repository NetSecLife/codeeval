import sys

def isPrime(a):
    if a > 1:
        for i in range(2,a):
            if (a % i) == 0:
                return False
        else:
            return True
def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        primecount = 0
        n1, n2 = test.strip().split(',')
        n1 = int(n1)
        n2 = int(n2)
        for i in range(n1, n2):
            if isPrime(i):
                primecount += 1
        print(primecount)
    test_cases.close()

main()