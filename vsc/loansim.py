set path=C:\Program Files\nodejs\

borrowing_frequency = input("Total number of times borrowed: ")
borrowing_value = 0
loan = input("Total amount borrowed: ")
interest = input("Fixed interest rate: ")
sim_duration = input("Duration of simulation: ")
interest_payment = 0
total_interest = 0
total_payments = 0
monthly_payment = 0
total_value = 0
interval_withdrawal = loan/borrowing_frequency
academic_year_length = 9
year_length = 12
total_installments = 12
month = 0
#bills are spaced roughly 3 months apart

def calculate_monthly_payment(x,y):
    float(borrowing_frequency,loan,interest)
    intervals = 9/borrowing_frequency
    monthly_payment = ((borrowing_value)/10)
    print("Month" month ": $" monthly_payment + (borrowing_value * interest))
    borrowing_value = borrowing_value + (borrowing_value * interest)
    return borrowing_value

while academic_year_length > 0:
    for i in academic_year_length:
        if (academic_year_length % borrowing_frequency = 0) == True:
            borrowing_value = borrowing_value + 1
            print("Withdrawal #" borrowing_value)
            print("$"interval_withdrawal)
            calculate_monthly_payment(borrowing_frequency,borrowing_value)

        academic_year_length = academic_year_length - 1
        monthly_payment = loan/120
        