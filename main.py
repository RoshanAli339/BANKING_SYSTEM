#Author: Shaik Roshan Ali


import os
import random as r
import datetime
import openpyxl
import new_user
import existing

def start():
    print('\t\t\tBANKING SYSTEM')

    print('1.Existing user\n2.New user')
    choice = int(input('Enter your choice: '))
    
    if choice == 1:
        existing.user()
    elif choice == 2:
        new_user.creating()


start()
    