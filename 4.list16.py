# Program to print all even numbers in a range
start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))

even_numbers_in_range = [num for num in range(start_range, end_range + 1) if num % 2 == 0]
print(f"All even numbers in the range [{start_range}, {end_range}]: {even_numbers_in_range}")
