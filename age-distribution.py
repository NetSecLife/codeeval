import sys

def main():
    test_cases = open(sys.argv[1],'r')
    for test in test_cases:
        test = int(test)
        if test >= 0 and test <= 2:
            print("Still in Mama's arms")
        elif test >= 3 and test <= 4:
            print("Preschool Maniac")
        elif test >= 5 and test <= 11:
            print("Elementary school")
        elif test >= 12 and test <= 14:
            print("Middle school")
        elif test >= 15 and test <= 18:
            print("High school")
        elif test >= 19 and test <= 22:
            print("College")
        elif test >= 23 and test <= 65:
            print("Working for the man")
        elif test >= 66 and test <= 100:
            print("The Golden Years")
        else:
            print("This program is for humans")
    test_cases.close()
main()