# Program to find the cube sum of first n natural numbers
n = int(input("Enter the value of n: "))
cube_sum = ((n * (n + 1)) // 2) ** 2
print(f"The cube sum of first {n} natural numbers is: {cube_sum}")
