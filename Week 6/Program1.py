def to_binary_representation(number):
    if number < 0:
        raise ValueError("Input must be a positive integer")
    return bin(number)[2:]


# Example usage:

binary_representation = to_binary_representation(10)
print(binary_representation)
