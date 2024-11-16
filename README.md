# Star School

The Star School is a software application designed to help schools manage their students. It provides a terminal design with easy access and intuitive usability. All pages have clear instructions on how to navigate through the system.

The user will be able to add, update information, delete and view a list of students.

![Welcome Page]()

Visit the deployed site here: [Star School]()

Access data from googlesheets (view only): [Google Sheets Data](https://docs.google.com/spreadsheets/d/1CCOi1AUOKehff-ohgTwe3t93eIQz85yU5-M2x407v5E/edit?usp=sharing)

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

## Testing

**Testing Input**
| Test | Outcome |
|--|--|
|All input text and numbers sending data correctly| Pass |
|All inputs validate data correctly| Pass|
|Prevent user from sending incorrect data| Pass |

> No Issues reported from the users

### Bugs

- When a user interacts with students data (add,update,delete), it does not update the table, unless the user leaves the application and runs again.

### Validator Testing

- Python
    - No major error returned when passing except by Long line. Most of the lines were adjusted to fit Pip8, but I opted to not fix some of them for readability purposes.

    ![Pyhton]()

## Deploying to Heroku  

Heroku has been used to deploy this project as Python is used as a back-end language. To allow for accurate testing, I deployed the project to Heroku early on using Automatic Deployment to update the program every time new code was pushed to my GitHub repository. Here are the steps that I followed to set my project up, guidance was provided by the [Code Institute's](https://codeinstitute.net/ie/) 'Love Sandwiches' project.     

1. Log in to [Heroku](https://id.heroku.com/login) or create an account if you are a new user.
2. Once logged in, in the Heroku Dashboard, navigate to the '**New**' button in the top, right corner, and select '**Create New App**'.
<details>
<summary>Create new app</summary>
</details>  

3. Enter an app name and choose your region. Click '**Create App**'.
<details>
<summary>Enter app name</summary>
</details>  
  
4. In the Deploy tab, click on the '**Settings**', reach the '**Config Vars**' section and click on '**Reveal Config Vars**'. Here you will enter KEY:VALUE pairs for the app to run successfully. In KEY enter `CREDS`, in VALUE, paste in the text content of your `CREDS.json` file. Select '**Add**'.  
5. Repeat this process with a KEY:VALUE pair of `PORT` and `8000`.
6. In the Settings tab, in the Buildpack section, click '**Add Buildpack**', located near the bottom, right of the refreshed screen. One at a time, choose the '**Python**' pack, save changes, then choose the '**NodeJS**' buildpack and save changes. **NB: the Python buildpack _must_ be above the NodeJS buildpack.**
  
<details>
<summary>Choose Buildpacks</summary>
</details>  
  
7. Go to the '**Deploy**' tab and choose GitHub as the Deployment method.
8. Search for the repository name, select the branch that you would like to build from, and connect it via the '**Connect**' button.
9. Choose from '**Automatic**' or '**Manual**' deployment options, I chose the 'Automatic' deployment method. Click '**Deploy Branch**'.
10. Once the waiting period for the app to build has finished, click the '**View**' link to bring you to your newly deployed site. 

## Credits

### Content
>**Code Institute** Love Sandwiches Project Walkthrough     

>  General lookup for Pyhton taken from [w3 school](https://www.w3schools.com/python/)
