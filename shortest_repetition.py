import sys

def short_rep(lines):
    substring = ''
    lines = lines.rstrip()
    for char in lines:
        substring += char
        if len(lines) % len(substring) == 0:
            if int((len(lines) / len(substring))) * substring == lines:
                print(len(substring))
                break

def main():
    test_cases = open(sys.argv[1], 'r')
    for i in test_cases:
        short_rep(i)
    test_cases.close()
main()

#LOGIC FLOW

#Grab input, parse line to shortest_rep func
#For loop through chars adding to substring, test substring to see if len of lines modulus len of substring is 0
#If 0 then further test the string to make sure it is the period
#Do this by comparing length makeup of the various strings, if equals len of lines then is period
#Break out of loop after reporting the length of the substring

#Algorithm taken from
#http://stackoverflow.com/questions/19779071/detect-string-repetition-in-python-without-regular-expression


