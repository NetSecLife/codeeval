import sys

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        result = ""
        a,b,c = test.split(' ')
        for x in range(1,int(c)+1):
            if (x % int(a) == 0) and (x % int(b) == 0):
                result += "FB "
            elif x % int(b) == 0:
                result += "B "
            elif x % int(a) == 0:
                result += "F "
            else:
                result += str(x) + " "
        result = result[:-1]
        print(result)

    test_cases.close()

main()


#split the inpput into 3 variables
#use third variable + 1 to define the for range and create al lthe numbers needed
#perform if statements on the numbers
#append results to result, add spaces, print result, cut off final space
