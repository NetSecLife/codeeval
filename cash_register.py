import sys

value_list = [10000, 5000, 2000, 1000, 500, 200, 100, 50, 25, 10, 5, 1]

Values_to_words = {
    1: 'PENNY',
    5: 'NICKEL',
    10: 'DIME',
    25: 'QUARTER',
    50: 'HALF DOLLAR',
    100: 'ONE',
    200: 'TWO',
    500: 'FIVE',
    1000: 'TEN',
    2000: 'TWENTY',
    5000: 'FIFTY',
    10000: 'ONE HUNDRED'
}

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        test_string = test.strip()
        result = []
        PP = int(float(test_string.split(";")[0])*100)
        CH = int(float(test_string.split(";")[1])*100)
        change = CH - PP
        if change == 0:
            print("ZERO")
            continue
        if change < 0:
            print("ERROR")
            continue
        for value in value_list:
            if change >= value:
                change -= value
                result.append(Values_to_words[value])
        print(','.join(result))
    test_cases.close()

main()


#Calculate the change that has to be returned to the customer (f2 -f1)
#Lets assume 0.06 return
#Expand numbers into int so 6
#For loop  through value list, checking if change is >= to val
#If true then change = change - val, until no change left to be given
#Append the name of whatever to be given back
#Print result