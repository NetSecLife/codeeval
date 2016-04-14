import sys
import collections

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        lst = test.strip().split(' ')
        count = collections.Counter(lst)
        uni = [i for i, v in count.items() if v == 1]
        print(lst.index(min(uni)) + 1 if uni else 0)
main()