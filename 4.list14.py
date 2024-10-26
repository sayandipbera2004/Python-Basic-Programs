# Program to print even numbers in a list
def print_even_numbers(lst):
    even_numbers = [num for num in lst if num % 2 == 0]
    return even_numbers

# Input from the keyboard
my_list = [int(x) for x in input("Enter space-separated elements of the list: ").split()]
even_numbers = print_even_numbers(my_list)
print(f"The even numbers in the list are: {even_numbers}")
