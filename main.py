# Get user input
credit_score = int(input("Enter your credit score: "))
annual_income = float(input("Enter your annual income: "))
loan_amount = float(input("Enter the loan amount you're requesting: "))
# Define the loan qualification criteria
min_credit_score = 700
min_annual_income = 25000
max_loan_amount = 100000

# Check if the user qualifies for the loan
if credit_score >= min_credit_score and annual_income >= min_annual_income and loan_amount <= max_loan_amount:
    print("Congratulations! You qualify for the loan.")
else:
    print("Sorry, you do not qualify for the loan.")
