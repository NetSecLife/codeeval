import sys

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        low_count, total, high_count = 0, 0, 0
        for i in test:
            if i.isupper():
                high_count += 1
                total += 1
            elif i.islower():
                low_count += 1
                total += 1
        high_percent = format((high_count / total * 100), '.2f')
        low_percent = format((low_count / total * 100), '.2f')
        print('lowercase: ' + low_percent + ' ' + "uppercase: " + high_percent)
    test_cases.close()

main()