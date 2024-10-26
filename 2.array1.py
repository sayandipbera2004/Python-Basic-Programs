# Program to find the sum of an array
def array_sum(arr):
    return sum(arr)

# Input from the keyboard
array = [int(x) for x in input("Enter space-separated elements of the array: ").split()]
print(f"The sum of the array is: {array_sum(array)}")
