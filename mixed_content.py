import sys

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        dec_list = []
        alp_list = []
        splitlist = test.strip().split(',')
        for i in splitlist:
            if i.isdecimal():
                dec_list.append(i)
            elif i.isalpha():
                alp_list.append(i)
        if len(alp_list) == 0:
            print(','.join(dec_list))
        elif len(dec_list) == 0:
            print(','.join(alp_list))
        else:
            print(','.join(alp_list) + '|' + ','.join(dec_list))
    test_cases.close()
main()



#split input into list sep by ,
#for loop through
#if alpha then add to alpha list
#if dec then add to dec list
#rejoin lists at end