import sys

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        word, char = test.strip().split(',')
        index = 0
        for i in range(0,len(word)):
            if word[i] == char:
                index = i
        if index != 0:
            print(index)
        else:
            print("-1")
main()




#split the input into a word, and a letter to be found
#for loop through the word, reporting the index of each time this char is seen.
#report the final index seen of this char which will be the rightmost char