# Program to reverse a list
def reverse_list(lst):
    return lst[::-1]

# Input from the keyboard
my_list = [int(x) for x in input("Enter space-separated elements of the list: ").split()]
reversed_list = reverse_list(my_list.copy())  # Copy to keep the original list
print(f"The reversed list is: {reversed_list}")
