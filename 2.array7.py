# Program to check if the given array is monotonic
def is_monotonic(arr):
    increasing = decreasing = True

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            decreasing = False
        elif arr[i] < arr[i - 1]:
            increasing = False

    return increasing or decreasing

# Input from the keyboard
array = [int(x) for x in input("Enter space-separated elements of the array: ").split()]
print(f"Is the array monotonic? {is_monotonic(array)}")
