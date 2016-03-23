import sys

def main():
    test_cases = open(sys.argv[1], 'r')
    for i in test_cases:
        words = i.split()
        words.reverse()
        print(' '.join(words))
    test_cases.close()

main()