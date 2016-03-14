def isPrime(a):
    if a > 1:
        for i in range(2,a):
            if (a % i) == 0:
                return False
        else:
            return True

def main():
    primesum = 0
    primesumcount = 0
    overallcount = 0
    while primesumcount < 1000:
        if isPrime(overallcount):
            primesum += overallcount
            primesumcount += 1
            overallcount += 1
        else:
            overallcount +=1
    print(primesum)

main()


#while loop prime sum count under 1000
#check if num is prime
#if prime then add to primesum
#add one onto primesumcount
#add one onto overall count
#elif not prime just add one to overall count
#repeat