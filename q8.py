import random

# Generate a random 4-digit binary number (0s and 1s)
binary_number = ''.join(random.choice(['0', '1']) for _ in range(4))
print("Generated 4-digit binary number:", binary_number)

# Convert the binary number to base 10
decimal_number = int(binary_number, 2)
print("Equivalent base 10 number:", decimal_number)
