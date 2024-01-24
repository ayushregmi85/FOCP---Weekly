def find_factors(number):
    if number <= 0:
        raise ValueError("Input must be a positive integer")
    factors = [i for i in range(1, number + 1) if number % i == 0]
    return factors


factors_of_12 = find_factors(12)
print(factors_of_12)
