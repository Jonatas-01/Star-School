import gspread
from google.oauth2.service_account import Credentials
import os

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('star_school')

students = SHEET.worksheet('students')
data = students.get_all_values()

def welcome_page():
    """
     Display the Welcome Page to customer
    """
    clear_terminal()
    print(r"""
         ______   ________   ________   ________      ______   __   __     _____   ________   ________   __
        /   ___) |__    __| |   __   | |   __   |    /   ___) |  | |  |   /   __| |   __   | |   __   | |  |
       (   (__      |  |    |  |__|  | |  |__| _/   (   (__   |  |_|  |  /   /    |  |  |  | |  |  |  | |  |
        \__   \     |  |    |   __   | |   __   \    \__   \  |   _   | (   (     |  |  |  | |  |  |  | |  |
        ___)   )    |  |    |  |  |  | |  |  |  |    ___)   ) |  | |  |  \   \__  |  |__|  | |  |__|  | |  |_____
       (______/     |__|    |__|  |__| |__|  |__|   (______/  |__| |__|   \_____| |________| |________| |________|
    """)
    print("Welcome to Star School!")
    print("Here you can have access to manage all students data.")
    main_menu()


def clear_terminal():
    """
     Clear the terminal
    """
    os.system("clear") # clear the terminal


def view_students():
    """
     Display all students data
    """
    print("View all students data")
    # Print the data
    for row in data:
        print(row)
    
    while True:
        try:
            print("""
            Please choose from the following options:

            1.Back to Main Menu.
            2.Exit.
            """)
            # Get user's choise
            choice = int(input("Enter you choice:"))
            if choice == 1:
                clear_terminal()
                print("Returning to Main Menu...")
                main_menu()
                break
            elif choice == 2:
                clear_terminal()
                break
            else:
                clear_terminal()
                print("Invalid input. Please enter a number between 1 and 2.")
        except:
            clear_terminal()
            print("Invalid input. Please enter a number between 1 and 2.")

def main_menu():
    """
     Display the Main Menu to customer
    """
    print("""
    Main Menu:
    Please choose from the following options:

    1. View all students data
    2. Add new student data
    3. Update student data
    4. Delete student data
    5. Exit
    """)
    while True:
    # Get the user's choice
        try:
            choice = int(input("Enter your choice (1-5): "))
            if choice == 1:
                clear_terminal()
                view_students()
                break
            elif choice == 2:
                print(f"Option {choice} choosed")
                break
            elif choice == 3:
                print(f"Option {choice} choosed")
                break
            elif choice == 4:
                print(f"Option {choice} choosed")
                break
            elif choice == 5:
                print("Exiting...")
                break
            else:
                clear_terminal()
                print("Invalid input. Please enter a number between 1 and 5.")
                main_menu()

        except ValueError:
            clear_terminal()
            print("Invalid input. Please enter a number between 1 and 5.")
            main_menu()
            break


welcome_page()

