# Program to print odd numbers in a list
def print_odd_numbers(lst):
    odd_numbers = [num for num in lst if num % 2 != 0]
    return odd_numbers

# Input from the keyboard
my_list = [int(x) for x in input("Enter space-separated elements of the list: ").split()]
odd_numbers = print_odd_numbers(my_list)
print(f"The odd numbers in the list are: {odd_numbers}")
