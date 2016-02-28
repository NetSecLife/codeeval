"""
 In this challenge you're given a random string containing hidden and visible digits.
 The digits are hidden behind lower case latin letters as follows: 0 is behind 'a', 1 is behind ' b ' etc., 9
 is behind 'j'. Any other symbol in the string means nothing and has to be ignored. So the challenge is to
 find all visible and hidden digits in the string and print them out in order of their appearance.
 https://www.codeeval.com/open_challenges/122/
"""

import sys

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        result = ""
        for x in test:
            #Check if char is a decimal, if so add to result
            if x.isdecimal():
                result += x
            #Check if char is lower, if so further test it to see if a-j, and add to result as decimal
            elif x.islower():
                if x <= 'j':
                    b = ord(x) - 97
                    result += str(b)
        if result == "":
            print("NONE")
        print(result)
    test_cases.close()

main()

#a = 0; a = 97
#j = 9
#use ord(variable) - 97 to make the letter represent number

# for loop through the string
# decide if string is num, if so add it onto result
# decide if string is lowercase alphabet number
# if letter a-j then change it into a number
# append number to the result
# report result back