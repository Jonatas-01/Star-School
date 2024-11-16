# Star School

The Star School is a software application designed to help schools manage their students. It provides a terminal design with easy access and intuitive usability. All pages have clear instructions on how to navigate through the system.

The user will be able to add, update information, delete and view a list of students.

![Welcome Page]()

Visit the deployed site here: [Star School]()

Access data from googlesheets (view only): [Google Sheets Data]()

## User Stories

### User
> As a user I want to be able to have access to a list of all students.   
> As a user I want to be able to add new students.    
> As a user I want to be able to update any information of the students.  
> As a user I want to be able to delete students from my data.    
> As a user I want to be able to go back to the menu any time I want.   
> As a user I want a clear terminal on each page.   

### Business Owner
> As a software owner I want to provide a clean design to users.    
> As a software owner I want to provide all the data the user needs.     
> As a software owner I want to provide to user the ability to add, update, and delete data.     
> As a software owner I want to prevent users from sending invalid inputs.   
> As a software owner I want to facilitate the data management to the user. 

## Features

- __The Welcome Page__

    - Feature will appears first time the user run the code.
    - Welcome Page has a welcoming text and a draw "Star School".
    - Bellow welcome text has main menu.

    ![Welcome Page]()

- __Main Menu__

    - Feature will first appear under the welcome page and later every time the user presses to return to the main menu.
    - The main menu displays options to the user: View all student's data, add new student data, update student data, delete student data, and exit.
    - User will directed to tha page chosen.

    ![Main Menu]()

- __View Students__

    - View students displays all students data in a table format, each student is placed in a row.
    - This feature will appear when the user inputs "1" in the terminal while in the main menu, and when all pages update students information.
    - When choosing to view students from the main menu, an option to return to the main menu or exit will appear under the students display.

    ![View Students]()

- __Add Student__

    - Add student will display instructions on how to send data in CSV format, and the option to return to the main menu.
    - Feature will appear when the user input "2" in the main menu.
    - After data validation, the value will be stored in Google Sheets and give the option to return to the main menu or exit.

    ![Add Student]()

- __Update Student Data__

    - Update Student will display options of what data want to update. The options are: Name, Student Number, Age, Year Grade, and Test Scores. It will also display the option to return to the main menu or exit.
        - All options to update data have validation, instructions on how to send data, and only change the data chosen.
    - Feature will appear when the user input "3" in the main menu.
    - After data validation, the value will be updated in Google Sheets and give the option to return to the main menu or exit.

    ![Update Student Data]()

- __Delete Student Data__

    - Delete Student Data will display a list of all students and each student in a row.
    - Feature will appear when the user input "4" in the main menu.
    - The user will need to select the row to delete or press ENTER to back to the main menu.

    ![Delete Student Data]()

- __Exit__

    - Exit will display a goodbye message and make user leave the application. 
    - Feature will appear when the user input "5" in the the main menu.

    ![Exit]()

## Skeleton Plane

- __Flowchart:__
    A detailed flowchart was created to outline the user journey and application logic.
    
    ![Flowchart]()

- __Google API:__
    Prior to starting any program function code, the relevant Credentials and API setup took place. Security was a crucial factor in connecting to a Google Account to access the Google Sheets worksheet. Guidance for setting up these authorizations and credentials was provided through the Code Institute's Full Stack Software Development course.

- __Google Sheets:__
    Used to store my data, simulating a database. All data entry and manipulation occur within the terminal, and the user interacts with a clear and straightforward CLI.

    ![Google Sheet]()

- __Desing:__
    The entire program is displayed in a Command Line Interface (CLI). The application is designed to be user-friendly with clear prompts and validations to guide users through various tasks such as adding income, recording expenses, and generating summaries.