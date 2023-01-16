def test_case_1():
    bal = float(input("please input the outstanding balance of your credit card?"))#asks the balance
    annual_rate = float(input("Please input the annual interest rate"))#asks the annual inerest rate
    month_pay = float(input("Please input the minimum monthly payment rate "))#ask the minimum monthly payment

    for month in range(0, 12):#we use a for loop to compute until thr 12th month
        month = month + 1
        print("month:", month)#counts months

        Minimum_monthly_payment = bal * (month_pay / 100)
        Interest_Paid = (annual_rate / 100) / 12 * bal
        Principal_paid = Minimum_monthly_payment - Interest_Paid
        bal = bal - Principal_paid#calculates accoding to instructions and updates balance after each months

        print("Minimum Monthly Payment", Minimum_monthly_payment)
        print("Interest paid,", Interest_Paid)
        print("principal paid", Principal_paid)
        print("Remaining Balance", bal)#prints calculations



def test_case_2():
    bal = float(input("please input the outstanding balance of your credit card?"))
    annual_rate = float(input("Please input the annual interest rate"))
    month_pay = 4#here we used the same code but we locked the minimum interest rate at 4 %

    for month in range(1, 13):
        month = month + 1
        print("month:", month)

        Minimum_monthly_payment = bal * (month_pay / 100)
        Interest_Paid = (annual_rate / 100) / 12 * bal
        Principal_paid = Minimum_monthly_payment - Interest_Paid
        bal = bal - Principal_paid

        print("Minimum Monthly Payment", Minimum_monthly_payment)
        print("Interest paid,", Interest_Paid)
        print("principal paid", Principal_paid)
        print("Remaining Balance", bal)

test_case_1()
test_case_2()

