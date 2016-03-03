import sys

def main():
    test_cases = open(sys.argv[1], 'r')
    for i in test_cases:
        result = ""
        for b in i:
            if b.islower():
                result += b.upper()
            elif b.isupper():
                result += b.lower()
            else:
                result += b
        print(result)

main()