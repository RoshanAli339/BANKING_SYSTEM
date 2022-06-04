import os
from datetime import datetime
import random as r
import openpyxl

def creating():
    os.system('clear')
    print('Please enter the following details correctly for avoiding re-corrections!')
    name = input('Name: ')
    fname = input('Father name: ')
    mname = input('Mother name: ')
    gender = input('Gender(M/F/O): ')
    DOB = input('Date of birth: ')
    age = input('Age: ')
    address = input('Address: ')
    phone = input('Phone number: ')
    aadhar = input('Aadhar number: ')
    security = input('Enter a security pin: ')
    re = input('Re enter security pin: ')
    while security != re:
        security = input('Both the entries did not match! Enter a security pin: ')
        re = input('Re enter security pin: ')
    acc_num = str(int((r.random()) * (10 ** 10)))


    print('This is your account number. Please take a note of it for future usage of your account: ', acc_num)
    details = {'name':name, 'account':acc_num, 'father':fname, 'mother':mname, 'address':address,
                    'gender':gender,'dob':DOB, 'age':age,  'phone':phone, 'aadhar':aadhar, 'pin':security, 'date':datetime.today()}
                
    wb = openpyxl.load_workbook('details.xlsx')
    sh = wb['Sheet1']
    row = sh.max_row + 1
    i = 1
    for detail in details.values():
        sh.cell(row, i, value=detail)
        i += 1
    
    wb.save('details.xlsx')

    accounts = {'name':name, 'account':acc_num, 'dob':DOB, 'gender':gender, 'father':fname, 'pin':security, 
                        'balance':0.0}
    wb = openpyxl.load_workbook('accounts.xlsx')
    sh = wb['Sheet1']
    row = sh.max_row + 1
    i = 1
    for detail in accounts.values():
        sh.cell(row, i, value=detail)
        i += 1
    
    wb.save('accounts.xlsx')