from typing import List

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        # Step 1: Sieve of Eratosthenes to find all primes up to `right`
        def sieve_of_eratosthenes(limit):
            sieve = [True] * (limit + 1)
            sieve[0], sieve[1] = False, False  # 0 and 1 are not prime numbers
            for start in range(2, int(limit**0.5) + 1):
                if sieve[start]:
                    for i in range(start * start, limit + 1, start):
                        sieve[i] = False
            return sieve

        # Step 2: Generate primes up to `right`
        sieve = sieve_of_eratosthenes(right)
        
        # Step 3: Collect primes in the range [left, right]
        primes_in_range = [i for i in range(left, right + 1) if sieve[i]]
        
        # Step 4: If fewer than 2 primes exist in the range, return [-1, -1]
        if len(primes_in_range) < 2:
            return [-1, -1]
        
        # Step 5: Find the closest pair of primes in the range
        min_diff = float('inf')
        best_pair = [-1, -1]
        
        for i in range(len(primes_in_range) - 1):
            num1 = primes_in_range[i]
            num2 = primes_in_range[i + 1]
            diff = num2 - num1
            if diff < min_diff:
                min_diff = diff
                best_pair = [num1, num2]
        
        # Return the closest pair of primes
        return best_pair
