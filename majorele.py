import sys
from collections import Counter

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        strlist = test.strip().split(',')
        sortlist = Counter(strlist)
        c = 0
        for i in sortlist:
            if sortlist[i] > (len(sortlist) / 2):
                print(i)
                c = 1
        if c == 0:
            print("None")
    test_cases.close()
main()




#For loop through the list
#Count each number
#If number is over listlength/2 then print it
#Otherwise print None if none of numbers over l/2
