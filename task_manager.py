# importing libraries
import re
from datetime import datetime, date


# USER DEFINED FUNCTIONS

# Displaying Main Menu
def main_menu(status):
    """This function will return to main menu"""

    print(f"\n\033[1;4mMAIN MENU\033[0m")

    if status == "admin":

        option = input('''
s   - Statistics
r   - Registering a user
a   - Adding a task
va  - View all tasks
vm  - view my tasks
e   - Exit

Select an option from above: ''').lower()

    else:
        option = input('''
a   - Adding a task
va  - View all tasks
vm  - view my tasks
e   - Exit

Select an option from above: ''').lower()

    return option

# Register a new user
def reg_user(usernames):
    """This function will create a new user"""

    # New username
    new_user = input("Enter a new username here: ")

    while True:

        if new_user == "":
            new_user = input("You haven't entered anything, please try again: ")

        elif new_user in usernames:
            new_user = input("This username already exists, please create an alternative: ")

        else:
            print("Username saved")
            break

    return new_user

# Display conditions for creating a new password
def passw_cond():
    """This function will just print out the conditions for a new password
       and ask the user to enter a desired password"""

    new_pword = input("""
\033[1;4mConditions for a valid password:\033[0m

1 - Should have atleast one number
2 - Should have atleast one uppercase and one lowercase character
3 - Should have atleast one special character
4 - Should be between 6 and 20 characters in length

Enter your new password here: """)

    return new_pword

# Creating a new password
def reg_pword(new_user):
    """This function will create a new password and then
       write the new login credentials to user.txt"""

    new_pword = passw_cond()

    while True:

        regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"

        # Compiling regular expressions
        pat = re.compile(regex)

        # Searching regular expressions
        mat = re.search(pat, new_pword)

        # Validating conditions
        if mat:
            break

        elif new_pword == "":
            print("\nYou haven't entered anything, please try again\n")
            new_pword = passw_cond()

        else:
            print("\nPassword invalid, please try again\n")
            new_pword = passw_cond()

    # Password confirmation
    cfirm_password = input("Please confirm your new password: ")

    while True:

        if cfirm_password == new_pword:
            print("New password saved, user registered successfully!")
            break

        elif cfirm_password == "":
            cfirm_password = input("You haven't entered anything, please try again: ")

        else:
            cfirm_password = input("Passwords do not match, try again: ")

    # Writing new user details to user.txt file
    file1 = open('user.txt', 'a')
    file1.write(f"\n{new_user}, {cfirm_password}")
    file1.close()

# Validate date input format
def validate_date():
    """This function will validate a string
       date's format entered by the user"""

    due = input("Task due date (dd short month in words yyyy): ")

    try:
        dateObject = datetime.strptime(due, '%d %b %Y')
        return due

    except ValueError:
        return False

# Display this message when nothing is entered by user
def blank_inp_msg():
    """This function will display an error message
       if and when user input is blank"""

    err_msg = input("You haven't entered anything, please try again: ")

    return err_msg


# Reading in login details from user.txt file
usernames = []
passwords = []

with open('user.txt', 'r') as f:
    for line in f:
        temp = line.strip()
        l = temp.split(', ')
        usernames.append(l[0])
        passwords.append(l[1])


# REGISTERED USER LOGIN SECTION
login = False

username = input("Username: ")

# Validating username
while True:

    if username == "":
        username = blank_inp_msg()

    elif username not in usernames:
        username = input("User not registered, please try again: ")

    else:
        break

password = input("Password: ")

# Validating password
i = 1
while i <= 4:

    if password == "":
        password = input(f"You haven't entered anything, please try again ({4-i} attempts remaining): ")
        i += 1

    elif password not in passwords:
        password = input(f"Incorrect username/password combination, please try again ({4-i} attempts remaining): ")
        i += 1

    elif passwords.index(password) != usernames.index(username):
        password = input(f"Incorrect username/password combination, please try again ({4-i} attempts remaining): ")
        i += 1

    elif password in passwords:
        print(f"\nWelcome {username}!")
        login = True
        break

else:
    print("\nYour attempts have run out, program will exit!")


if login:

    # MAIN MENU
    while True:

        menu = main_menu(username)

        # Display stats
        if menu == 's':

            # Number of registered users
            total_users = len(usernames)

            # Number of task entries recorded
            count = 0
            with open('tasks.txt', 'r') as file:

                for line in file:
                    count += 1

            output = f"""
\033[1;4mCompany Name (Pty) Ltd Statistics Report\033[0m

Registered Users           {total_users}
Recorded Tasks             {count}
------------------------------------------"""

            # Output
            print(output)

        # Register new user
        elif menu == 'r':
            new_user = reg_user(usernames)
            usernames.append(new_user)
            reg_pword(new_user)

        # Add new task
        elif menu == 'a':

            # Assigned user
            user = input("Username of employee to whom task will be assigned: ")

            while True:

                if user == "":
                    user = blank_inp_msg()

                elif user not in usernames:
                    reg_new_user = input("The user name entered is not registered. Register new user? (yes/no): ").lower()

                    if reg_new_user == "":
                        reg_new_user = blank_inp_msg()

                    elif reg_new_user == "y" or reg_new_user == "yes":
                        new_user = reg_user(usernames)
                        usernames.append(new_user)
                        reg_pword(new_user)
                        break

                    elif reg_new_user == "n" or reg_new_user == "no":
                        print("\nReturning to main manu...")
                        break

                else:

                    # Task title
                    task_title = input("Title of task: ").title()

                    while True:

                        if task_title == "":
                            task_title = blank_inp_msg().title()

                        else:
                            break

                    # Task description
                    task_description = input("Enter a short description of the task: ").title()

                    while True:

                        if task_description == "":
                            task_description = blank_inp_msg().title()

                        else:
                            break

                    # Task assigned date
                    today = date.today()
                    task_date = today.strftime('%d %b %Y')
                    print(task_date)

                    # Task due date
                    task_due_date = validate_date()

                    while True:

                        if task_due_date:
                            print("Date saved")
                            break

                        elif not task_due_date:
                            print("Incorrect date format, please try again with advised format")
                            task_due_date = validate_date()

                    # Default completion status
                    completed = "No"

                    # Writing new task details to tasks.txt file
                    file = open('tasks.txt', 'a')
                    file.write(f"\n{user}, {task_title}, {task_description}, {str(task_date)}, {str(task_due_date)}, {completed}")
                    file.close()

                    break

        # View all tasks
        elif menu == 'va':

            print(f"\n\033[1;4mALL TASKS\033[0m")

            # Opening tasks.txt file and reading all lines
            with open('tasks.txt', 'r') as file:

                for line in file:
                    temp = line.strip()
                    l = temp.split(', ')

                    # Specifying output layout
                    output = f"""_______________________________________________________
Tasks:              {l[1]}
Assigned to:        {l[0]}
Date assigned:      {l[3]}
Due date:           {l[4]}
Completed:          {l[5]}
Task description:   {l[2]}"""

                    # Output
                    print(output)

        # View current logged-in user's tasks
        elif menu == 'vm':

            print(f"\n\033[1;4mYour tasks:\033[0m")

            my_tasks = []
            x = 1

            # Opening tasks.txt file and reading all lines
            with open('tasks.txt', 'r') as file:

                for line in file:
                    temp = line.strip()
                    l = temp.split(', ')

                    # Appending all task entries registered under
                    # logged-in user's name to list 'my_tasks'
                    if l[0] == username:
                        my_tasks.append(l)

                        # Specifying output layout
                        output = f"""
Task {x}:             {l[1]}
Assigned to:        {l[0]}
Date assigned:      {l[3]}
Due date:           {l[4]}
Completed:          {l[5]}
Task description:   {l[2]}
____________________________________________"""

                        # Output
                        print(output)

                        # Updating counters
                        x += 1

                # If logged-in user has no task entries
                if len(my_tasks) == 0:
                    print(f"There are currently no task entries for {username}.\n")

        # Exit program
        elif menu == 'e' or menu == 'exit':
            print("goodbye!")
            exit()

        else:
            print("Unknown input, please Try again: ")

# End of program
