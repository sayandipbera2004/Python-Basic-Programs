# Program for Reversal algorithm for array rotation
def reverse_array(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def rotate_array_reversal(arr, d):
    n = len(arr)
    reverse_array(arr, 0, d - 1)
    reverse_array(arr, d, n - 1)
    reverse_array(arr, 0, n - 1)
    return arr

# Input from the keyboard
array = [int(x) for x in input("Enter space-separated elements of the array: ").split()]
rotation_distance = int(input("Enter the rotation distance: "))
rotated_array = rotate_array_reversal(array, rotation_distance)
print(f"The array after rotating by {rotation_distance} positions: {rotated_array}")
