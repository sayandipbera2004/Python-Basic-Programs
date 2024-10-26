# Program to swap two elements in a list
def swap_elements(lst, i, j):
    if 0 <= i < len(lst) and 0 <= j < len(lst):
        lst[i], lst[j] = lst[j], lst[i]
    return lst

# Input from the keyboard
my_list = [int(x) for x in input("Enter space-separated elements of the list: ").split()]
index1 = int(input("Enter the index of the first element to swap: "))
index2 = int(input("Enter the index of the second element to swap: "))
swapped_list = swap_elements(my_list, index1, index2)
print(f"The list after swapping elements at positions {index1} and {index2}: {swapped_list}")
