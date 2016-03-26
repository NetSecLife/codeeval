import sys

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        t1, t2 = test.strip().split('|')
        t1 = t1.strip()
        t2 = t2.strip()
        count = 0
        for i in range(len(t1)):
            if t1[i] == t2[i]:
                continue
            else:
                count +=1
        if count <= 2 and count > 0:
            print("Low")
        elif count <= 4 and count > 2:
            print("Medium")
        elif count <= 6 and count > 4:
            print("High")
        elif count > 6:
            print("Critical")
        else:
            print("Done")
    test_cases.close()

main()