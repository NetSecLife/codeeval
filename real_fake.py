import sys

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        test = test.strip()
        test = list(test.replace(" ", ""))
        res = 0
        for i in range(0, len(test), 2):
            res += int(test[i]) * 2
        for i in range(1, len(test), 2):
            res += int(test[i])
        if (res % 10) == 0:
            print('Real')
        else:
            print('Fake')
    test_cases.close()
    
main()



#Double every third number starting from the first one
#Add them together
#Add them to those figures that were not doubled
#If total sum of all numbers is divisible by 10 without remainder then real