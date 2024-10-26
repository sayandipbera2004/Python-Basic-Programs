# Program to find the sum of elements in a list
def sum_of_elements(lst):
    return sum(lst)

# Input from the keyboard
my_list = [int(x) for x in input("Enter space-separated elements of the list: ").split()]
total_sum = sum_of_elements(my_list)
print(f"The sum of elements in the list is: {total_sum}")
