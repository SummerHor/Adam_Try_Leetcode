import math


def is_prime(num: int):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    limit = int(math.sqrt(num))
    for i in range(3, limit + 1, 2):
        if num % i == 0:
            return False
    return True


def find_prime(nums):
    prime_list = []

    for i in range(int(math.sqrt(nums)) + 1):
        if is_prime(i):
            prime_list.append(i)
    return prime_list


def count_prime(nums):
    count = 0
    found_prime = find_prime(nums)
    listing_prime = []  # To track the actual primes found

    if nums < 2:
        return count

    for i in range(2, nums):
        isPrime = True
        for prime in found_prime:
            if i == prime:
                break
            if i % prime == 0:
                isPrime = False
                break

        if isPrime:
            count += 1
            listing_prime.append(i)

    return count, listing_prime


# Example Check
print(count_prime(10))
# Output: (4, [2, 3, 5, 7]) -> 9 is now correctly excluded!
