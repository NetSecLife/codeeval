import sys

slang = [
    ', yeah!', ', this is crazy, I tell ya.',
    ', can U believe this?', ', eh?', ', aw yea.',
    ', yo.', '? No way!', '. Awesome!'
]

def main():
    test_cases = open(sys.argv[1], 'r')
    count = 0
    for i in test_cases:
        slang_word = ""
        used = 0
        for e in i:
            if ("!" in e or "?" in e or "." in e) and (used == 0):
                slang_word += slang[count]
                count += 1
                used = 1
            elif ("!" in e or "?" in e or "." in e) and (used == 1):
                slang_word += e
                used = 0
            else:
                slang_word += e
            if count == 7:
                count = 0
        print(slang_word.rstrip('\n'))

main()

#rough logic
#setup dictionary with slang words
#setup count variable, for each word add on 1, once it hits 7 then reset count to 0
#take word input
#for loop through words looking for . or ! or ?
#if! ? . in e then add on thing
#alternate between every other
