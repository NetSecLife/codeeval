# INFO: https://www.codeeval.com/open_challenges/237/
import sys

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        #Split the strings
        split_string = test.split('|')
        hex_string = split_string[0].split(' ')
        binary_string = split_string[1].split(' ')
        #Remove any whitespace entries inside of the lists
        hex_string = [x for x in hex_string if x]
        binary_string = [x for x in binary_string if x]
        #Convert the strings into decimal
        decimal_hex = 0
        for x in hex_string:
            decimal = int(x, 16)
            decimal_hex = decimal_hex + decimal
        decimal_binary = 0
        for b in binary_string:
            decimal = int(b, 2)
            decimal_binary = decimal_binary + decimal
        #Compare the two numbers and report if virus detected
        if decimal_binary == decimal_hex:
            print("True")
        elif decimal_binary > decimal_hex:
            print("True")
        elif decimal_binary < decimal_hex:
            print("False")

    test_cases.close()

main()


#split strings into seperate strings
#convert them to decimal
#sum them
#perform comparisions
#report results