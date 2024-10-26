# Program to find the largest number in a list
def find_largest_number(lst):
    return max(lst)

# Input from the keyboard
my_list = [int(x) for x in input("Enter space-separated elements of the list: ").split()]
largest_number = find_largest_number(my_list)
print(f"The largest number in the list is: {largest_number}")
