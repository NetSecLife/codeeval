import sys
import string

def main():
    test_cases = open(sys.argv[1],'r')
    for test in test_cases:
        a = test.lower()
        i = string.ascii_lowercase
        res = []
        for b in i:
            if b not in a:
                res.append(b)
        if len(res) == 0:
            print("NULL")
        else:
            print(''.join(res))
    test_cases.close()
main()

#take input
#lower the string
#if x of string.ascii_lowercase not in the string
#push letters not in to result
#print result