# Program to check Armstrong Number
num = int(input("Enter a number: "))
order = len(str(num))
sum = 0
temp = num

while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10

if num == sum:
    print(f"{num} is an Armstrong Number.")
else:
    print(f"{num} is not an Armstrong Number.")
