''' 3. Write and test a function that determines if a given integer is a prime number. A
prime number is an integer greater than 1 that cannot be produced by multiplying
two other integers.'''


def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    if n <= 3:
        return True   # 2 and 3 are prime numbers
    
    # Eliminate even numbers and multiples of 3
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # Check for factors from 5 to the square root of n
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    
    return True

if __name__ == "__main__":
    test_numbers = [1, 2, 3, 4, 5, 16, 17, 18, 19, 20]
    for number in test_numbers:
        result = is_prime(number)
        print(f"{number} is prime: {result}.")
