#Author: Shaik Roshan Ali


''' 
    A main file which executes the main part of the program.
    This file does not have any special importance as I wished to keep it separated for different operations
    This file imports the other two main files :
                                                    new_user.py which creates and updates the information of new users.
                                                    existing.py which deals with all the functions that are related to an existing user.
'''


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
    