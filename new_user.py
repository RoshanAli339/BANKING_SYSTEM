import os

#the datetime module is used to save the date and time of creation of the user account
from datetime import datetime

#the random module is used to generate random 10 digit account numbers for the new users
import random as r

#the openpyxl module is used to deal with the accounts.xlsx file and the details.xlsx files where the data is being stored
import openpyxl


#the only method where the creation of the user is taking place and the data is being updated to the excel files

def creating():
    os.system('cls')

    #Taking input all the essential or required details of the user
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

    #the security pin is asked for re verification and if the pin does not match then the user will be prompted again to enter the security pin
    security = input('Enter a security pin: ')
    re = input('Re enter security pin: ')
    while security != re:
        security = input('Both the entries did not match! Enter a security pin: ')
        re = input('Re enter security pin: ')

    # a random 10 digit number is being generated for the account number of the user
    # A DRAWBACK
    # the recurring of two accounts with same account number is imminent and might cause errors
    acc_num = str(int((r.random()) * (10 ** 10)))

    #printing the generated account number for the user to make a note of it
    print('This is your account number. Please take a note of it for future usage of your account: ', acc_num)
    
    #opening the details.xlsx file and appending the data that has been taken as input 
    #this file contains the personal information of the user
    wb = openpyxl.load_workbook('details.xlsx')
    sh = wb['Sheet1']
    sh.append([name, acc_num, fname, mname, address, gender, DOB, age, phone, aadhar, security, datetime.today()])
    wb.save('details.xlsx')

    #opening the accounts.xlsx file and appending the account data essential for the transactions 
    #this file stores only the information of users necessary for the transactions to take place
    wb = openpyxl.load_workbook('accounts.xlsx')
    sh = wb['Sheet1']
    sh.append([name, acc_num, DOB, gender, fname, security, 0.0])
    
    wb.save('accounts.xlsx')