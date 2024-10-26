# Program to multiply all numbers in the list
def multiply_all_numbers(lst):
    result = 1
    for num in lst:
        result *= num
    return result

# Input from the keyboard
my_list = [int(x) for x in input("Enter space-separated elements of the list: ").split()]
product = multiply_all_numbers(my_list)
print(f"The product of all numbers in the list is: {product}")
