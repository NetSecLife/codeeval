import sys

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        test = test.strip()
        wordlist = list(test)
        for i in test:
            if wordlist.count(i) == 1:
                print(i)
                break
    test_cases.close()

main()


#Count occurrences of chars
#For loop through word
#Compare char to occurrences of chars
#if 1 == complete
#break