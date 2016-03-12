import sys

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        list1, list2 = test.strip('\n').split('|')
        wines = list1.strip().split(' ')
        letters = list2.strip().lower()
        res = []
        for wine in wines:
            word = wine
            match = True
            for letter in letters:
                if letter not in wine.lower():
                    match = False
            if match == True:
                res.append(word)
        if len(res) > 0:
            print(' '.join(res))
        else:
            print("False")

if __name__ == '__main__':
    main()


#split into lists seperated by the |
#further split wine into sep words
#for loop through wines
#test each word for the letters
#if letters are not in the word then set to untrue and pass the loop
#if letters are in the word then match remains true and prints out the original word
#print out results