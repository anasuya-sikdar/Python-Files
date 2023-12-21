#Anasuya sikdar
#Assignment 7

import csv
import datetime

def startUp():
    'Reads the accounts.csv file and returns a dictionary of account details'
    infile = open('accounts.csv', 'r')
    lineList = infile.readlines()
    infile.close()
    
    accounts = {}
    for line in lineList:
        pin, first_name, last_name, balance = line.strip().split(',')
        accounts[pin] = [first_name, last_name, float(balance)]
    
    return accounts


def verifyPin(d):
    attempts = 3
    while attempts > 0:
        pin = input("Enter Pin number: ")
        if pin in d:
            return (pin, d[pin][0])
        else:
            attempts -= 1
            print('Invalid pin, try again:')
    return (None, 'Please call customer support at 800-000-0000')

def displayMenu(name):
    print(f"{name}")
    print("1. Deposit")
    print("2. Withdrawal")
    print("3. Balance")
    print("4. Quit")
    return verifyMenuChoice()

def verifyMenuChoice():
    while True:
        try:
            choice = int(input("Enter your choice 1, 2, 3 or 4: "))
            if choice in [1, 2, 3, 4]:
                return choice
            else:
                print("Enter 1 or 2 or 3 or 4, try again.")
        except ValueError as e:
            print(f"{e} invalid choice, non-numeric characters not allowed, try again.")

def verifyAmount():
    while True:
        try:
            amount = float(input("Enter the amount: "))
            if amount < 0:
                print("Negative amount. Try again.")
            else:
                return amount
        except ValueError:
            print("Invalid amount. Use digits only.")

def deposit(pin, d):
    amount = verifyAmount()
    d[pin][2] += amount
    return

def withdraw(pin, d):
    while True:
        amount = verifyAmount()
        if amount > d[pin][2]:
            print("Insufficient funds to complete the transaction")
        else:
            d[pin][2] -= amount
            return

def balance(pin, d):
    return d[pin][2]

def quit(pin, d):
    response = input("Do you wish to leave the transaction? (y/n): ")
    if response == 'y':
        receipt(pin, d)
    return response

def receipt(pin, d):
    print("\n   ABC Bank Branch Receipt   ")
    print("         123 Aloha St.")
    print("         Anytown, USA\n")
    print(f"Date: {datetime.date.today()}")
    print(f"Name: {d[pin][0]} {d[pin][1]}")
    print(f"Available Balance: ${d[pin][2]:,.2f}\n")
    print("Thank you for using the ABC Banking System")
    print("'Goodbye'")

def tester():
    dict = startUp()   #dictionary
    print()
    if dict == None:
        return
    pin, msg = verifyPin(dict)
    if pin == None:
        print(msg)
        return 'Goodbye'
    name = msg
    
    while True:
        print()
        choice = displayMenu(name)
        if choice == 1:
            deposit(pin, dict)
        elif choice == 2:
            withdraw(pin, dict)
        elif choice == 3:
            b = balance(pin, dict)
            msg = 'Current balance is: ${:,.2f}'
            print('\n',msg.format(b))
        elif choice == 4:
            reply = quit(pin, dict)
            if reply == 'n':
                pass
            else:
                return 'Goodbye'
    return


tester()
