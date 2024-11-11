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

welcome_page()
