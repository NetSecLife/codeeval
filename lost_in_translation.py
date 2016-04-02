import sys

code = {
    'a': 'y',   'b': 'h',   'c': 'e',   'd': 's',
    'e': 'o',   'f': 'c',   'g': 'v',   'h': 'x',
    'i': 'd',   'j': 'u',   'k': 'i',   'l': 'g',
    'm': 'l',   'n': 'b',   'o': 'k',   'p': 'r',
    'q': 'z',   'r': 't',   's': 'n',   't': 'w',
    'u': 'j',   'v': 'p',   'w': 'f',   'x': 'm',
    'y': 'a',   'z': 'q'}

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        test = test.strip()
        res = ' '
        for i in test:
            if i == ' ':
                res += ' '
            else:
                res += code[i]
        print(res)
    test_cases.close()

main()