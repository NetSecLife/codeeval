import sys
import json

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        test = test.strip()
        lst = 0
        for item in json.loads(test)['menu']['items']:
            if item and 'label' in item:
                lst += (item['id'])
        print(lst)
    test_cases.close()

main()