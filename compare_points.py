import sys

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        cords = test.split(" ")
        loc = ""
        if cords[3] > cords[1]:
            loc += "N"
        elif cords[3] < cords[1]:
            loc += "S"
        if cords[0] > cords[2]:
            loc += "W"
        elif cords[0] < cords[2]:
            loc += "E"
        if loc == "":
            print("here")
        print(loc)
    test_cases.close()
main()


#split the input into cords, compare the indexs of the cords and append to result
#print result