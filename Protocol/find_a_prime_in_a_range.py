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


import math
import numpy
import time

def prime2(lower=3,upper=1000000):
    return filter(lambda num: numpy.array([num % factor for factor in range(lower,1+int(math.sqrt(num)))]).all(), range(lower,upper+1))

def prime3(lower=3,upper=1000000):
    return filter(lambda num: (num % numpy.arange(lower,1+int(math.sqrt(num)),2)).all(), range(lower,upper+1,2))

def prime6(lower=3,upper=1000000):
    primes = numpy.arange(lower, upper + 1, 2)
    isprime = numpy.ones((upper - 1) / 2, dtype=bool)
    for factor in primes[:int(math.sqrt(upper))]:
        if isprime[(factor - 2) / 2]: isprime[(factor * 3 - 2) / 2::factor] = 0
    return numpy.insert(primes[isprime], 0, 2)

def prime7(lower=3,upper=1000000):
    for num in range(lower, upper + 1):
       # all prime numbers are greater than 1
       if is_prime(num):
           for i in range(2, num):
               if (num % i) == 0:
                   break
           else:
               print(num)
def next_prime(num):
    if (not num & 1) and (num != 2):
        num += 1
    if is_prime(num):
        num += 2
    while True:
        if is_prime(num):
            break
        num += 2
    return num

def is_prime(num):
    if num == 2:
        return True
    if not num & 1:
        return False
    return pow(2, num-1, num) == 1


if __name__ == "__main__":
    lower = pow(2, 1023)
    upper = pow(2, 1024)
    #primelist=list(prime2(lower,upper))
    #primelist=prime7(lower,upper)
    print (" The next prime number after %s is:" %lower)
    start_time = time.perf_counter()
    p = next_prime(lower)
    q = next_prime(p)
    print("p:",p,"\n","q:",q)
    end_time = time.perf_counter()
    print("it takes:", end_time - start_time)
