import sys
from datetime import datetime

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        time1, time2 = test.strip('\n').split(' ')
        FMT = '%H:%M:%S'
        time1 = datetime.strptime(time1,FMT)
        time2 = datetime.strptime(time2,FMT)
        if time1 > time2:
            delta_time = time1 - time2
        elif time2 > time1:
            delta_time = time2 - time1
        print(delta_time)
    test_cases.close()
    
main()