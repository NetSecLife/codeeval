import sys

def compress_seq(seq):
    seq = seq.split(" ")
    res = []
    count = 0
    last = 0
    for i in seq:
        if i == last:
            count += 1
        else:
            res.append(str(count))
            res.append(last)
            last = i
            count = 1
    res.append(str(count))
    res.append(last)
    res = res[2:]
    print(" ".join(res))

def main():
    test_cases = open(sys.argv[1], 'r')
    for line in test_cases:
        compress_seq(line)
main()

#Take user input
#Pass lines to compress_seq
#Convert string into list
#Setup variable that holds what the 'last' number was
#Count the seqeuence by comparing the new number to the last and adding 1 to count if same
#Append count / last number to result list once the new number is not equal to the last number
#Rest count to 1 and last to the new number
#Repeat
#Print results showing count and sequenced number
