#Anasuya Sikdar
#Assignment 4.1

def student_loan(amount,rate,years):
    #Converting Annual rate into Monthly rate and years into months
    monthly_rate = rate / (12 *100)
    months = years * 12

    #Calculate the Monthly payment
    payment = (monthly_rate * amount)/(1 - (1 + monthly_rate)** -months)

    #Initializing balance and total interest variable
    balance = amount
    paid_total_interest = 0

    #Open file for writing                                            
    outfile = open("loanSchedule.csv", 'w')
    outfile.write('Prepared by: Anasuya Sikdar')
    outfile.write('\n')
    outfile.write('Payment Number, Payment, Interest, Principal, Balance, Total Interest')
    outfile.write('\n')
    for month in range(1, months + 1):
        interest = monthly_rate * balance
        principal = payment - interest
        balance -= principal
        paid_total_interest += interest

        #Write it to the csv file
        formatStr = '{:2},{:.2f},{:.2f},{:.2f},{:.2f},{:.2f}\n'
        outfile.write(formatStr.format(month, payment, interest, principal, balance, paid_total_interest))
        #Close the file
    outfile.close()

    #Print summary statement
    print(f"If you had ${amount:,.2f} in student loans at {rate}% and a {years}-year term, your monthly"
          f"payments would be ${payment:,.2f}. Over the life of your loan, you would repay a total"
          f"of ${amount + paid_total_interest:,.2f}; interest charges would cause your balance to grow by ${paid_total_interest:,.2f}. \n"
          f"To view monthly detail go to student_loan.csv")
                                       
    #Return the thank you message
    return 'Thank you for using the student_loan() function'


