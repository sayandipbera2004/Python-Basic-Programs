# Program to find the n-th Fibonacci number
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Enter the value of n: "))
result = fibonacci(n)
print(f"The {n}-th Fibonacci number is: {result}")
