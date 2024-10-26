# Program to split the array and add the first part to the end
def split_and_add(arr, k):
    return arr[k:] + arr[:k]

# Input from the keyboard
array = [int(x) for x in input("Enter space-separated elements of the array: ").split()]
split_position = int(input("Enter the split position: "))
result_array = split_and_add(array, split_position)
print(f"The array after splitting at position {split_position} and adding to the end: {result_array}")
