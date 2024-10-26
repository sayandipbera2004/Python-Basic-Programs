# Different ways to clear a list in Python
def clear_list(lst):
    # Method 1: Clear the list using clear() method
    lst.clear()

    # Method 2: Assign an empty list to the original list
    # lst = []

    return lst

# Input from the keyboard
my_list = [int(x) for x in input("Enter space-separated elements of the list: ").split()]
cleared_list = clear_list(my_list.copy())  # Copy to keep the original list
print(f"The list after clearing: {cleared_list}")
