#
# lower = pow(2,1023)
# upper = pow(2,1024)
#
# print("Prime numbers between", lower, "and", upper, "are:")
#
# for num in range(lower, upper + 1):
#    # all prime numbers are greater than 1
#    if num > 1:
#        for i in range(2, num):
#            if (num % i) == 0:
#                break
#        else:
#            print(num)

import random
import time
import sys
sys.path.append(".")
from checkPrime import checkPrime


def find_prime_q():
    q_lower = pow(2, 159)
    q_upper = pow(2, 160)
    for q in range(q_lower, q_upper):
        if checkPrime.miller_rabin(q):
            return q

def find_both_primes():
    p_lower = pow(2, 1023)
    p_upper = pow(2, 1024)
    q = find_prime_q()
    for i in range (1,4096):
        M = random.randrange(p_lower,p_upper)
        Mr = M %2*q
        p = M-Mr +1
        if checkPrime.miller_rabin(p):
            return (p,q)
        else:
            find_prime_q()


if __name__ == "__main__":
    print ("The calculation of primes started")
    start_time = time.perf_counter()
    (p,q) = find_both_primes()
    print("p:",p,"\n","q:",q)
    end_time = time.perf_counter()
    print("it takes:", end_time - start_time)
