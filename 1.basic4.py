# Program to calculate simple interest
principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time (in years): "))
simple_interest = (principal * rate * time) / 100
print(f"Simple Interest is: {simple_interest}")
