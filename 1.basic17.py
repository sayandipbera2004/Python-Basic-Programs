# Program to find the sum of squares of first n natural numbers
n = int(input("Enter the value of n: "))
sum_of_squares = (n * (n + 1) * (2 * n + 1)) // 6
print(f"The sum of squares of first {n} natural numbers is: {sum_of_squares}")
