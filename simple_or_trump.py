"""The rules are also simple: an ace beats a deuce (2) unless it is a trump deuce.
input is in form of
AD 2H | H
KD KH | C
JH 10S | C

winners of above would be
2H
KD KH
JH
"""

import sys


def main():
    #Declare dictionary that holds the rankings of cards
    ranking = {'2':'2',    '3':'3',    '4':'4',
               '5':'5',    '6':'6',    '7':'7',
               '8':'8',    '9':'9',    '10':'10',
               'J':'11',   'Q':'12',   'K':'13',
               'A':'14'}
    #Take the input
    test_cases = open(sys.argv[1], 'r')
    #For loop through the inputs
    for test in test_cases:
        #Split the input
        hand = test.split()

        #Setup hand 1 variables
        hand1 = str(hand[0])
        hand1suit = hand1[-1:]
        hand1 = hand1[:-1]

        #Setup hand 2 variables
        hand2 = str(hand[1])
        hand2suit = hand2[-1:]
        hand2 = hand2[:-1]

        #Setup deuce
        deuce = hand[3]

        #Perform comparisons
        hand1isWinner = 0
        hand2isWinner = 0
        tie = 0

        #Compare the ranking of the cards
        if int(ranking[hand1]) > int(ranking[hand2]):
            hand1isWinner = 1
        elif int(ranking[hand1]) < int(ranking[hand2]):
            hand2isWinner = 1
        elif int(ranking[hand1]) == int(ranking[hand2]):
            tie = 1

        #check for trump
        if hand1suit == deuce and hand2suit == deuce:
            pass
        elif hand1suit == deuce:
            hand1isWinner = 1
            hand2isWinner = 0
        elif hand2suit == deuce:
            hand1isWinner = 0
            hand2isWinner = 1

        #print winner result
        if hand1isWinner == 1:
            print(hand[0])
        elif hand2isWinner == 1:
            print(hand[1])
        elif tie == 1:
            print(hand[0],hand[1])

    test_cases.close()


main()


#for test
#split into three variables, hand1, hand2, deuce
#cut off the last letter of hand 1 / 2 into hand1suit / hand2suit

#compare the hand values, then check if a deuce trumps the values
#report back which hand won

#could use class to hold the hand values?
#expand into classes if the score is low