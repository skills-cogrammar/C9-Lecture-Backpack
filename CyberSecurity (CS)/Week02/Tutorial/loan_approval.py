income = 40000
credit_score = 700

if (income > 20000 and credit_score > 600):
    loan_approval = "Approved"
elif (income <= 20000 and credit_score > 600):
    loan_approval = "Loan Approved"
else:
    loan_approval = "Not Approved"

print(loan_approval)
