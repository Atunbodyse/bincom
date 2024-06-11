def recursive_search(numbers, target, index=0):
    if index >= len(numbers):
        return False
    if numbers[index] == target:
        return True
    return recursive_search(numbers, target, index + 1)

# Example list of numbers
numbers_list = [5, 8, 2, 10, 15]

# Ask the user for the number to search
target_number = int(input("Enter the number to search for: "))

# Call the recursive search function
result = recursive_search(numbers_list, target_number)

if result:
    print(f"The number {target_number} is present in the list.")
else:
    print(f"The number {target_number} is not found in the list.")
