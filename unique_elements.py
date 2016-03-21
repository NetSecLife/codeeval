import sys

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        res = []
        last = ""
        test = test.strip('\n').split(',')
        for i in test:
            if i == last:
                pass
            else:
                last = i
                res.append(i)
        print(','.join(res))
    test_cases.close()

main()


#for loop through line
#if i == last then pass
#otherwise add to res