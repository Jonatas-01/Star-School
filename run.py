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
         ______   ________   ________   ________       ______     _____   __    __   ________   ________   __
        /   ___) |__    __| |   __   | |   __   |     /   ___)   /   __| |  |  |  | |   __   | |   __   | |  |
       (   (__      |  |    |  |__|  | |  |__| _/    (   (__    /   /    |  |__|  | |  |  |  | |  |  |  | |  |
        \__   \     |  |    |   __   | |   __   \     \__   \  (   (     |   __   | |  |  |  | |  |  |  | |  |
        ___)   )    |  |    |  |  |  | |  |  |  |     ___)   )  \   \__  |  |  |  | |  |__|  | |  |__|  | |  |_____
       (______/     |__|    |__|  |__| |__|  |__|    (______/    \_____| |__|  |__| |________| |________| |________|
    """)
    print("Welcome to Star School!")
    print("Here you can have access to manage all students data.")
    main_menu()


def clear_terminal():
    """
     Clear the terminal
    """
    os.system("clear") # clear the terminal


def exit_program():
    """
     Exit the program
    """
    clear_terminal()
    print("Thank you for using Star School!")
    print("Goodbye!")  


def return_to_main_menu():
    """
     Return to the main menu
    """
    while True:
        try:
            print("""
            Please choose from the following options:

            1.Return to Main Menu.
            2.Exit.
            """)
            # Get user's choise
            choice = int(input("Enter you choice: "))
            if choice == 1:
                clear_terminal()
                print("Returning to Main Menu...")
                main_menu()
                break
            elif choice == 2:
                exit_program()
                break
            else:
                clear_terminal()
                print("Invalid input. Please enter a number between 1 and 2.")
        except:
            clear_terminal()
            print("Invalid input. Please enter a number between 1 and 2.")


def view_students():
    """
     Display all students data
    """
    print("View all students data\n")
    # Print the data
    print(
        f"{'Name':<12}{'Student Number':<21}{'Age':<10}{'Year Grade':<15}{'Test-1':<10}{'Test-2':<10}{'Test-3':<10}"
        )
    for index, row in enumerate(data[1:], start=1):
        print(f"{index}. {row[0]:<12}{row[1]:<19}{row[2]:<10}{row[3]:<16}{row[4]:<10}{row[5]:<10}{row[6]:<10}")
    
    return_to_main_menu()


def add_student():
    """
    Get value from the user and update the worksheet
    """
    print("Add new student data")
    while True:
        # Get the student personal data from the user
        print("""
        Enter student personal data as the example bellow.
        Example: Name, Student number, Age, Year Grade.
                John,12345678,13,1
        """)

        # Get the student personal data from the user
        new_data = input("Enter student data: ")
        personal_data = new_data.split(",")

        # Validate the data

        if validate_data(personal_data):
            break
    
    # Update the worksheet
    print("Updating worksheet...")
    students.append_row(personal_data)
    print("Worksheet updated successfully!")

    return_to_main_menu()


def validate_data(values):
    """
    Inside the try, validades all 5 values from the user, update
    string to integer starting from second data and raise ValueError 
    if the data is invalid.
    """

    try:
        # Validate values, must be 4 values
        if len(values) != 4:
            clear_terminal()
            raise ValueError(
                f"Exactly 5 values required, you provided {len(values)}"
            )
        # Validate firt value, must be a string
        elif not values[0].isalpha():
            clear_terminal()
            raise ValueError(
                f"Name must be a string, you provided {values[0]}"
            )
        # Validate second value, must be a number and 8 digits long
        elif len(values[1]) != 8:
            clear_terminal()
            raise ValueError(
                f"Student number must be 8 digits long, you provided {len(values[1])}"
            )
        elif not values[1].isdigit() or values[0].isspace():
            clear_terminal()
            raise ValueError(
                f"Student number must be a number, you provided {values[1]}"
            )
        # Validate third value, must be a number
        elif not values[2].isdigit():
            clear_terminal()
            raise ValueError(
                f"Age must be a number, you provided {values[2]}"
            )
        # Validate fourth value, must be a number beetween 1 and 3
        elif not values[3].isdigit() or int(values[3]) < 1 or int(values[3]) > 3:
            clear_terminal()
            raise ValueError(
                f"Year Grade must be a number between 1 and 3, you provided {values[3]}"
            )
        else:
            for i in range(1, 4):
                values[i] = int(values[i])
            print("Data is valid!")
            return True
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False


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
                clear_terminal()
                print("""
                Please choose from the following options:

                1.Add new student personal data.
                2.Add student exams data.
                3.Return to Main Menu.
                4.Exit.
                """)
                while True:
                    try:
                        choice = int(input("Enter your choice (1-4): "))
                        if choice == 1:
                            clear_terminal()
                            add_student()
                            break
                        elif choice == 2:
                            print(f"Option {choice} choosed")
                            break
                        elif choice == 3:
                            clear_terminal()
                            main_menu()
                            break
                        elif choice == 4:
                            exit_program()
                            break
                        else:
                            clear_terminal()
                            print("Invalid input. Please enter a number between 1 and 4.")
                    except ValueError:
                        clear_terminal()
                        print("Invalid input. Please enter a number between 1 and 4.")
                break
            elif choice == 3:
                print(f"Option {choice} choosed")
                break
            elif choice == 4:
                print(f"Option {choice} choosed")
                break
            elif choice == 5:
                exit_program()
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

