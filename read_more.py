import sys

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        #Check if under or equal to 55 and print with no changes
        if len(test) <= 55:
            print(test)
        else:
            #Trim to 40 words
            test = test[:40]
            #Trim to last space and splice off last space
            test = test.rsplit(' ',1)[0]
            #Add on ... <Read More>
            test = test + "... <Read More>"
            print(test)

    test_cases.close()
main()

#https://www.codeeval.com/open_challenges/167/
#for through the text
#if under 55 chars then return the char
#else over 55 then splice the char
#rsplit off last word
#add on read more