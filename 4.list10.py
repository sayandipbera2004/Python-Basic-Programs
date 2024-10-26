# Program to find the smallest number in a list
def find_smallest_number(lst):
    return min(lst)

# Input from the keyboard
my_list = [int(x) for x in input("Enter space-separated elements of the list: ").split()]
smallest_number = find_smallest_number(my_list)
print(f"The smallest number in the list is: {smallest_number}")
