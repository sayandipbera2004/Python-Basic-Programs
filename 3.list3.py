# Ways to find the length of a list
def length_of_list(lst):
    return len(lst)

# Input from the keyboard
my_list = [int(x) for x in input("Enter space-separated elements of the list: ").split()]
list_length = length_of_list(my_list)
print(f"The length of the list is: {list_length}")
