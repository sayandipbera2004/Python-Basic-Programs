# Program for array rotation
def rotate_array(arr, d):
    return arr[d:] + arr[:d]

# Input from the keyboard
array = [int(x) for x in input("Enter space-separated elements of the array: ").split()]
rotation_distance = int(input("Enter the rotation distance: "))
rotated_array = rotate_array(array, rotation_distance)
print(f"The array after rotating by {rotation_distance} positions: {rotated_array}")
