import sys

def main():
    test_cases = open(sys.argv[1], 'r')
    for i in test_cases:
        result = ""
        a = i.rsplit()
        for z in a:
            n =''.join(z[0].upper() + z[1:])
            result = ' '.join([result, n])
        print(result[1:])
main()