# Program to print all odd numbers in a range
start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))

odd_numbers_in_range = [num for num in range(start_range, end_range + 1) if num % 2 != 0]
print(f"All odd numbers in the range [{start_range}, {end_range}]: {odd_numbers_in_range}")
