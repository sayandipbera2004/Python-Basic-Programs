# Program to find the second largest number in a list
def find_second_largest(lst):
    unique_numbers = list(set(lst))  # Remove duplicates
    unique_numbers.sort(reverse=True)
    if len(unique_numbers) >= 2:
        return unique_numbers[1]
    else:
        return "List does not have a second largest number."

# Input from the keyboard
my_list = [int(x) for x in input("Enter space-separated elements of the list: ").split()]
second_largest = find_second_largest(my_list)
print(f"The second largest number in the list is: {second_largest}")
