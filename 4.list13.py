# Program to find N largest elements from a list
def find_n_largest(lst, n):
    unique_numbers = list(set(lst))  # Remove duplicates
    unique_numbers.sort(reverse=True)
    return unique_numbers[:n]

# Input from the keyboard
my_list = [int(x) for x in input("Enter space-separated elements of the list: ").split()]
n = int(input("Enter the value of N: "))
n_largest_elements = find_n_largest(my_list, n)
print(f"The {n} largest elements in the list are: {n_largest_elements}")
