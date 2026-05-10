import math

# Using Sieve of Eratosthenes


def countPrime(n: int) -> int:
    if n < 3:
        return 0
    isPrime = [True] * n
    isPrime[0] = isPrime[1] = False
    for num in range(2, int(math.sqrt(n)) + 1):
        if isPrime[num]:
            for mul in range(num * num, n, num):
                isPrime[mul] = False
    return sum(isPrime)
