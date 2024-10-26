# Program to interchange first and last elements in a list
def interchange_first_last(lst):
    if len(lst) >= 2:
        lst[0], lst[-1] = lst[-1], lst[0]
    return lst

# Input from the keyboard
my_list = [int(x) for x in input("Enter space-separated elements of the list: ").split()]
interchanged_list = interchange_first_last(my_list)
print(f"The list after interchanging first and last elements: {interchanged_list}")
