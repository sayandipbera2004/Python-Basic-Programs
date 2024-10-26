# Program to check if a given number is a Fibonacci number
def is_perfect_square(num):
    square_root = int(num**0.5)
    return num == square_root**2

def is_fibonacci(num):
    return is_perfect_square(5 * num**2 + 4) or is_perfect_square(5 * num**2 - 4)

num = int(input("Enter a number: "))
if is_fibonacci(num):
    print(f"{num} is a Fibonacci number.")
else:
    print(f"{num} is not a Fibonacci number.")
