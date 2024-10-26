# Program to print all negative numbers in a range
start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))

negative_numbers_in_range = [num for num in range(start_range, end_range + 1) if num < 0]
print(f"All negative numbers in the range [{start_range}, {end_range}]: {negative_numbers_in_range}")
