import os
from datetime import datetime
from pydoc import doc
import random as r
import openpyxl

def creating():
    os.system('cls')
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
                
    wb = openpyxl.load_workbook('details.xlsx')
    sh = wb['Sheet1']
    sh.append([name, acc_num, fname, mname, address, gender, DOB, age, phone, aadhar, security, datetime.today()])
    wb.save('details.xlsx')

    wb = openpyxl.load_workbook('accounts.xlsx')
    sh = wb['Sheet1']
    sh.append([name, acc_num, DOB, gender, fname, security, 0.0])
    
    wb.save('accounts.xlsx')