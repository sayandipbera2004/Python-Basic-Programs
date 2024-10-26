# Program to calculate compound interest
principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time (in years): "))
compound_interest = principal * (1 + rate/100)**time - principal
print(f"Compound Interest is: {compound_interest}")
