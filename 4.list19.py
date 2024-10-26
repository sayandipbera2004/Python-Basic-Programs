# Program to print negative numbers in a list
def print_negative_numbers(lst):
    negative_numbers = [num for num in lst if num < 0]
    return negative_numbers

# Input from the keyboard
my_list = [int(x) for x in input("Enter space-separated elements of the list: ").split()]
negative_numbers = print_negative_numbers(my_list)
print(f"The negative numbers in the list are: {negative_numbers}")
