''' 2. Write and test a function that takes an integer as its parameter and returns the
factors of that integer. (A factor is an integer which can be multiplied by another to
yield the original).'''

#Python function that takes an integer as its parameter and returns a list of its factors.
def find_factors(n):
    if n <= 0:
        raise ValueError("Input must be a positive integer.")
    
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    
    return factors


if __name__ == "__main__":
    test_number = 28
    factors_of_test_number = find_factors(test_number)
    print(f"The factors of {test_number} are: {factors_of_test_number}.")
