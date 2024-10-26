# Program to find the remainder of array multiplication divided by n
def array_multiplication_remainder(arr, n):
    result = 1
    for num in arr:
        result = (result * num) % n
    return result

# Input from the keyboard
array = [int(x) for x in input("Enter space-separated elements of the array: ").split()]
divisor = int(input("Enter the divisor: "))
remainder = array_multiplication_remainder(array, divisor)
print(f"The remainder of array multiplication divided by {divisor} is: {remainder}")
