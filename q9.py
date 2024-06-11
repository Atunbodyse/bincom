
# Initialize variables to store the Fibonacci numbers
a, b = 0, 1
fib_sum = 0

# Sum the first 50 Fibonacci numbers
for _ in range(50):
    fib_sum += a
    a, b = b, a + b

print("The sum of the first 50 Fibonacci numbers is:", fib_sum)
