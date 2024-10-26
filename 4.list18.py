# Program to print positive numbers in a list
def print_positive_numbers(lst):
    positive_numbers = [num for num in lst if num > 0]
    return positive_numbers

# Input from the keyboard
my_list = [int(x) for x in input("Enter space-separated elements of the list: ").split()]
positive_numbers = print_positive_numbers(my_list)
print(f"The positive numbers in the list are: {positive_numbers}")
