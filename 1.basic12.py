# Program to find the n-th multiple of a number in the Fibonacci Series
def fibonacci_multiple(n, multiple):
    a, b = 0, 1
    count = 0
    while count < n:
        if a % multiple == 0:
            count += 1
        a, b = b, a + b
    return a

n = int(input("Enter the value of n: "))
multiple = int(input("Enter the multiple: "))
result = fibonacci_multiple(n, multiple)
print(f"The {n}-th multiple of {multiple} in the Fibonacci Series is: {result}")
