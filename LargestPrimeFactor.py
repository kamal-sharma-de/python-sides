def prime_factors(n):
    factors = []
    divisor = 2  # Start with the smallest prime number
    
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    
    return factors

 

if __name__ == "__main__":
  # Example: Get the prime factors of 13195
  number = 988185191081
  result = prime_factors(number)
  print("Prime factors of", number, ":", result)
  # The largest prime factor
  print("Larget prime factor of ", number, ":", result[-1])

