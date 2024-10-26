# Program to find the largest element in an array
def find_largest_element(arr):
    return max(arr)

# Input from the keyboard
array = [int(x) for x in input("Enter space-separated elements of the array: ").split()]
print(f"The largest element in the array is: {find_largest_element(array)}")
