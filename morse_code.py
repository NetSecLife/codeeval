import sys

morse = {'--...': '7', '---..': '8', '..-': 'U', '--.-': 'Q', '-..': 'D', '.--.': 'P', '-': 'T', '.-..': 'L',
         '.--': 'W', '--': 'M', '...-': 'V', '---': 'O', '...--': '3', '--..': 'Z', '----.': '9', '...': 'S',
         '-....': '6', '.---': 'J', '-.-.': 'C', '--.': 'G', '-.-': 'K', '-.--': 'Y', '....': 'H', '.-.': 'R',
         '.': 'E', '.....': '5', '..': 'I', '.----': '1', '..-.': 'F', '-----': '0', '-.': 'N', '-...': 'B',
         '.-': 'A', '..---': '2', '-..-': 'X', '....-': '4', ' ': ' '}

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        morselist = test.strip("\n").split(" ")
        result = ""
        for i in morselist:
            if i == '':
                result += ' '
            else:
                result += morse[i]
        print(result)
    test_cases.close()

main()