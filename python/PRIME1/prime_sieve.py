import sys
import math

# assumes that n is not even
def exhaustive_prime_check(n):
    i = 3
    while i <= math.sqrt(n):
        if n % i == 0: 
            return False
        i += 2
    return True

# if a number fails this test its definitely composite.
# if a number passes it is either prime or a Carmichael number.
def fermats_little_test(p):
    return ((2**p) % p) == 2

def is_prime(p):
    if fermats_little_test(p):
        return exhaustive_prime_check(p)
    else:
        return False

# construct a list of all the numbers 0 to n inclusive
# for each number up to the sqrt(n), if that number is prime,
# sieve out all multiples. return all non-zero list elements.
def primes_up_to(n):
    primes = [i for i in range(n+1)]
    primes[1]=0
    primes[2*2:n+1:2] = [0] * ((n/2)-1)
    for i in range(3, int(math.sqrt(n))+1):
        if is_prime(i):
            primes[2*i:n+1:i] = [0] * ((n/i)-1)
    return filter(None, primes)

# runs a little slower then the above, but interesting that it can be done almost as
# quickly without any explicit primality check
def primes_up_to_recursive(n):
    n = int(n)
    if n < 2:
        return []
    else:
        primes = primes_up_to_recursive(int(math.sqrt(n)))
        base = int(math.sqrt(n)) + 1
        next_primes = [ i for i in range(base, n+1) ]
        for prime in primes:
            first_multiple = base if base % prime is 0 else ((next_primes[0] + prime) / prime) * prime
            multiples = next_primes[first_multiple-base:(n+1)-base:prime]
            next_primes[first_multiple-base:(n+1)-base:prime] = [0]*len(multiples) # maye there is a more clever way of numerically determining length
        return primes + filter(None, next_primes)

def primes_in_range(start, end, sieve):
    start = max(start, 2)
    res = [n for n in range(start, end+1)]
    for prime in sieve:
        if prime <= math.sqrt(end):
            first_multiple = res[0] if res[0] % prime is 0 else (((res[0]+prime)/prime) * prime)
            first_index = first_multiple-start if first_multiple > prime else first_multiple + prime - start
            multiples = res[first_index:end+1-start:prime]
            res[first_index:end+1-start:prime] = [0]*len(multiples)
    return filter(None, res)

if __name__=="__main__":
    num_cases = int(sys.stdin.readline())
    cases = []
    for line in range(num_cases):
        case = sys.stdin.readline().split(" ")
        smallest, largest = int(case[0]), int(case[1])
        cases.append((smallest, largest))
    sieve = primes_up_to(int(math.sqrt(1000000000)))
    for start, end in cases:
        for prime in primes_in_range(start, end, sieve):
            print prime
        print
