"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-19 22:10:29
@Description: 
"""

import math
import time


def check_prime(n: int) -> bool:
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)), 2):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    primes = []
    t1 = time.time()
    number_range = range(100_000_000, 101_000_000)
    for possible_prime in number_range:
        if check_prime(possible_prime):
            primes.append(possible_prime)
    print("Took:", time.time() - t1)
    print(len(primes), primes[:10], primes[-10:])
