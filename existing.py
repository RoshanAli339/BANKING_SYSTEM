import os
from datetime import datetime
import openpyxl

def check_acc(ac, pin):
    wb = openpyxl.load_workbook(filename = 'accounts.xlsx')
    sh = wb['Sheet1']

    for i in range(2, sh.max_row+1):
        if sh.cell(i,2).value == ac:
            if sh.cell(i,6).value == pin:
                return i
            else: return 0
        else: return 0

def transfer(bal, ac):
    name = input("Enter name of recipient: ")
    bank = input("Enter recipient bank name and branch: ")
    acc = input("Enter account number of recipient: ")
    amount = float(input("Enter amount of money to be transferred: "))
    date = datetime.today()
    if amount > bal:
        print("Insufficient balance! The available balance is: Rs.", bal)
        exit(1)
    
    file = 'transacs//' + ac+ '.txt'
    f = open(file, 'a+')
    line = str(date) + ' Transfer: ' + 'Sent to: '+name+'\n'+('\t'*9)+' Bank: '+bank +'\n'+('\t'*9)+\
        ' Recipient account number: '+acc+'\n'+('\t'*9)+\
        ' Amount transferred: Rs.'+str(amount) + '\n'+('\t'*9)+' Available Balance: Rs.'+str(bal-amount)+'\n'
    f.write(line)
    f.close()
    print("Transfer successful! Remaining balance: Rs.", (bal-amount))
    return bal - amount

def deposit(bal, ac):
    amount = float(input('Enter the amount of money to deposit: Rs.'))
    file = 'transacs//' + ac + '.txt'
    date = datetime.today()
    f = open(file, 'a+')
    f.seek(0)
    line = str(date)+' Deposit: Balance before: Rs.'+str(bal)+'\n'+('\t'*9)+'Amount deposited: Rs.'+\
            str(amount)+'\n'+('\t'*9)+'Present balance: Rs.' + str(bal+amount) + '\n'
    f.write(line)
    f.close()
    print("Deposit successful! Remaining balance: Rs.", (bal+amount))
    return bal+amount

def withdraw(bal, ac):
    amount = float(input('Enter the amount of money to withdraw: Rs.'))
    if amount > bal:
        print('Insufficient balance! The available balance is: Rs.', bal)
        exit(1)
    file = 'transacs//' + ac + '.txt'
    date = datetime.today()
    f = open(file, 'a+')
    f.seek(0)
    line = str(date)+' Withdrawl: Balance before: Rs.'+str(bal)+str(bal)+'\n'+('\t'*9)+'    Amount withdrawn: Rs.'+\
        str(amount) + '\n'+('\t'*9)+'    Present balance: Rs.' + str(bal-amount) + '\n'
    f.write(line)
    f.close()
    print("Withdrawl successful! Remaining balance: Rs.", (bal-amount))
    return bal-amount
    
def user():
    os.system('clear')
    ac = input('Enter account number: ')
    pin = input('Enter security pin: ')

    row = check_acc(ac, pin)
    while row == 0:
        os.system('clear')
        print('Invalid account number or security pin!Enter \'e\' to exit or try again')
        ac = input('Enter account number: ')
        if ac == 'e':
            exit(1)
        pin = input('Enter security pin: ')
        row = check_acc(ac, pin)
    
    os.system('clear')
    print('LOGIN SUCCESSFUL!\n\n')

    wb = openpyxl.load_workbook(filename = 'accounts.xlsx')
    sh = wb['Sheet1']

    while True:
        print('1.Check balance\n2.Deposit money\n3.Withdraw money\n4.Transfer money\n5.Quit')
        choice = int(input('Enter your choice: '))

        if  choice == 1:
            print('Available balance: Rs.', sh.cell(row, 7).value)
        elif choice == 2:
            result = deposit(sh.cell(row, 7).value, ac)
            sh.cell(row, 7, value = result)
        elif choice == 3:
            result = withdraw(sh.cell(row, 7).value, ac)
            sh.cell(row, 7, value=result)
        elif choice == 4:
            result = transfer(sh.cell(row, 7).value, ac)
            sh.cell(row, 7, value=result)
        elif choice == 5:
            wb.save('accounts.xlsx')
            exit(0)
