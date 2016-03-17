import sys

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        listalph, listnum = test.strip('\n').split('|')
        listnum1 = listnum.split()
        result = []
        for i in listnum1:
            i = int(i)
            result += listalph[i-1]
        print(''.join(result))
    test_cases.close()

main()

#Split the input into two via pipe
#Further split nums into a list
#For loop through numbers
#Find the letters by referencing the for loop number as index - 1 to the first string
#Append the result to result list
#Join and print
