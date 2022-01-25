from RandomGenerator import RandomGenerator
import time
import random
from CheckPrime import CheckPrime

class FindInitialPrimeValues:
    def __init__(self):
        self.q_lower = pow(2, 159)
        self.q_upper = pow(2, 160)
        self.p_lower = pow(2, 1023)
        self.p_upper = pow(2, 1024)
    def find_prime_q(self):
        for q in range(self.q_lower, self.q_upper):
            if CheckPrime.miller_rabin(q):
                return q

    def find_both_primes(self):
        q = self.find_prime_q()
        for i in range (1,4096):
            M = random.randrange(self.p_lower,self.p_upper)
            Mr = M %2*q
            p = M-Mr +1
            if CheckPrime.miller_rabin(p):
                return p,q
            else:
                self.find_prime_q()


if __name__ == "__main__":
    print ("The calculation of primes started")
    primes = FindInitialPrimeValues()
    start_time = time.perf_counter()
    (p,q) = primes.find_both_primes()
    print("p:",p,"\n","q:",q)
    end_time = time.perf_counter()
    print("it takes:", end_time - start_time)
