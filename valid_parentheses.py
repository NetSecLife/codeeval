import sys

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        test = test.strip()
        true = 1
        length = len(test) /2
        if length.is_integer():
            length = int(length)
        else:
            print("False")
            continue
        for i in range(length):
            if test[i] == '(':
                if test[-i-1] == ')':
                    continue
                else:
                    true = 0
                    break
            if test[i] == '[':
                if test[-i-1] == ']':
                    continue
                else:
                    true = 0
                    break
            if test[i] == '{':
                if test[-i-1] == '}':
                    continue
                else:
                    true = 0
                    break
            else:
                true = 0
        if true == 1:
            print("True")
        else:
            print("False")
    test_cases.close()

main()