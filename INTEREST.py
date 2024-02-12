principal = float(input("Enter the principal amount: "))
interest_rate = float(input("Enter the annual interest rate (in percentage): "))
years = int(input("Enter the duration of the loan in years: "))

interest = principal * (interest_rate / 100) * years
total_amount = principal + interest
monthly_installment = total_amount / (years * 12)

print(f"Total interest: {interest} USD")
print(f"Total amount to be repaid: {total_amount} USD")
print(f"Monthly installment: {monthly_installment} USD")
