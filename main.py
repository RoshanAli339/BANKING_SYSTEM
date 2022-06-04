import os
import random as r
import datetime
import openpyxl
import new_user
import existing

def start():
    print('\t\t\tBANKING SYSTEM')
    '''xlsx_file = '//home//xtremer//Desktop//DEXTER_BANK//accounts.xlsx'
    wb = openpyxl.load_workbook(xlsx_file)
    sh = wb.create_sheet(index = 0, title='sheet 1')'''

    print('1.Existing user\n2.New user')
    choice = int(input('Enter your choice: '))
    
    if choice == 1:
        existing.user()
    elif choice == 2:
        new_user.creating()


start()
    