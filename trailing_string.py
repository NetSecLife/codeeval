import sys

def main():
    test_cases = open(sys.argv[1], 'r')
    for i in test_cases:
        l1, l2 = i.strip().split(",")
        l1 = l1.split(" ")
        l2 = l2.split(" ")
        if l1[-1] == l2[-1]:
            print('1')
        else:
            print('0')
    test_cases.close()

main()