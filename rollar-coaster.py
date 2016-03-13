import sys

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        binary = 0
        res = ""
        for i in test:
            if i.isalpha():
                if binary == 0:
                    res += i.upper()
                    binary = 1
                elif binary == 1:
                    res += i.lower()
                    binary = 0
            else:
                res += i
        print(res)
    test_cases.close()

main()


#for loop through the sentance
#switch between two if statements that change the letter to upper or lower depending on if alpha
