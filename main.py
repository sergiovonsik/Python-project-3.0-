import argparse
import math


parser = argparse.ArgumentParser()
parser.add_argument("--type", type=str, help="type")
parser.add_argument("--principal", type=int, help="the base")  # == P
parser.add_argument("--periods", type=int, help="the periods")  # == n
parser.add_argument("--interest", type=float, help="the interest")  # == "i" en bruto
parser.add_argument("--payments", type=int, help="the payments")  # == M
args = parser.parse_args()


if args.type == "diff":
    find_diff = {args.periods, args.principal, args.interest}
    if all(find_diff) == True:
        overpayment = 0
        for months_number in range(args.periods):
            months_number += 1
            if months_number == 1:
                i = args.interest / (12 * 100)
                d = args.principal / args.periods + i * args.principal
                d_rounded = math.ceil(d)
                print(f'Month {months_number}: payment is {d_rounded}')
                overpayment += d_rounded
            if months_number >= 2:
                i = args.interest / (12 * 100)
                d = args.principal / args.periods + i * (args.principal - ((args.principal * (months_number - 1)) / args.periods))
                d_rounded = math.ceil(d)
                print(f'Month {months_number}: payment is {d_rounded}')
                overpayment += d_rounded
        print(f'Overpayment = {overpayment - args.principal}')

    else:
        print('Incorrect parameters.')


# ------------------ANNUITY--------------------
if args.type == "annuity":

    find_payment = {args.periods, args.principal, args.interest}
    find_principal = {args.periods, args.payments, args.interest}
    find_months = {args.principal, args.payments, args.interest}

    if all(find_payment) == True: # FOR CHOICES = [PRINCIPAL; INTEREST; PERIODS] FIND PAYMENTS
        n = args.periods
        i = float(args.principal * args.interest / 100) / (12 * args.principal)
        payment = args.principal * (i * (1 + i) ** n) / ((1 + i) ** n - 1)
        payment = math.ceil(payment)
        print(f'Your annuity payment = {payment}!')
        overpayment_ = n * payment - args.principal
        print(f'Overpayment = {overpayment_}')

    elif all(find_principal) == True: # ANNUITY FOR CHOICES = [PAYMENTS; INTEREST; PERIODS] FIND PRINCIPAL
        n = args.periods
        i = args.interest / (12 * 100)
        principal = -(-(args.payments / ((i * math.pow((1 + i), n)) / (math.pow((1 + i), n) - 1))))
        print(f'Your loan principal = {math.ceil(principal)}!')
        overpayment_ = (n * args.payments) - principal
        print(f'Overpayment = {math.ceil(overpayment_)}')

    elif all(find_months) == True:
        # ANNUITY FOR CHOICES = [PAYMENTS; PRINCIPAL; INTEREST] FIND PERIODS
        loan_ppal = args.principal
        monthly_pay = args.payments
        loan_interest = args.interest
        i = float(loan_ppal * loan_interest / 100) / (12 * loan_ppal)
        i_ = (monthly_pay / (monthly_pay - i * loan_ppal))
        n = float((math.log(i_, (1 + i))))
        if n > 12:
            years = math.floor(n / 12)
            months = math.ceil(n % 12)
            if months == 12:  # if there are 12 month it became 1 more year
                years += 1
                months = 0
            if years == 1:  # quit or not "s" from years
                y_s = ""
            else:
                y_s = "s"

            if months == 1:  # quit or not "s" from months
                m_s = ""
            else:
                m_s = "s"
            if months > 0:
                print(f'It will take {years} year{y_s} and {months} month{m_s} to repay this loan!')
            elif months == 0:
                print(f'It will take {years} year{y_s} to repay this loan!')
            overpayment_ = (round(n) * args.payments) - args.principal
            print(f'Overpayment = {math.ceil(overpayment_)}')

    else:
        print('Incorrect parameters.')


