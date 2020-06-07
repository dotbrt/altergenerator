import json
import os
import random
from lenny import lenny

# Alterego generator is an app generating a random combination of first
# and last name and an avatar ready to use


## ASSETS ## 
with open('first-names.txt', 'r') as f1:
    first_names = json.load(f1)
with open('last-names.txt', 'r') as f2:
    last_names = json.load(f2)

### FUNCTIONS ###

def display_header():
    # Clears the terminal screen, and displays a title bar.
    os.system('clear')
              
    print("\t**********************************************")
    print("\t***  AlterGen - Alterego generator!  ***")
    print("\t**********************************************")
    
def get_user_choice():
    # Present a menu of available options
    print("\n[1] Choose a first name")
    print("[2] Choose a last name.")
    print("[3] Choose new identity.")
    print("[q] Quit.")
    
    return input("What would you like to do? \n")

def choose_first_name(first_names):
    # Chooses first name randomly
    return random.choice(first_names)

def choose_last_name(last_names):
    # Chooses last name randomly
    return random.choice(last_names)

def choose_both_names():
    # Chooses a random set of both first name and last name
    return random.choice(first_names), random.choice(last_names)

## MAIN PROGRAM ##
def main():
    # Variables storing choice  
    choice = ''
    f_name = ''
    l_name = ''
    display_header()
    while choice != 'q':

        #Asking user for a choice
        choice = get_user_choice()

        #Choice response
        display_header()
        if choice == '1':
            f_name = choose_first_name(first_names)
            print("\nHere's your new first name\n")
            print(f_name, l_name)
        elif choice == '2':
            l_name = choose_first_name(last_names)
            print("\nHere's your new last name\n")
            print(f_name, l_name)
        elif choice == '3':
            f_name = choose_first_name(first_names)
            l_name = choose_first_name(last_names)
            print("\nHere's your new alterego!\n")
            print(f_name, l_name, '\n', lenny())
        elif choice == 'q':
            print('q')
        else:
            print('\nWrong choice\n')
            print(f_name, l_name)


if __name__ == '__main__':
    main()