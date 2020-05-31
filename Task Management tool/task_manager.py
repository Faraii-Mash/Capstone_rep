#TaskManager.py
#Importing modules
import datetime
from datetime import date
#Open file for use in functions
#Opening a file
user_inquiry = open("user.txt", "r")

#Creating variables
user_name_list = ""
pass_word_list = ""

#for and in 
for user in user_inquiry:
    user = user.replace(" ", "")
    user = user.strip()
    user = user.split(",")
    #get user name and password into lists
    user_name_list += user[0]
    user_name_list += ","
    #
    pass_word_list += user[1]
    pass_word_list += "," 

user_name_list = user_name_list.split(",")
user_name_list = user_name_list[:-1] 

pass_word_list = pass_word_list.split(",")
pass_word_list = pass_word_list[:-1] 

#Define functions here
#Define login
def login():
    #declare varaible to check if password is correct 
    password_validate = False
    #login while not validated 
    while not password_validate:
        #Ask user for username and password to beigin program
        supplied_username = input("Please enter your username here: ")
        supplied_password = input("Please enter your password here: ")
        if (supplied_username in user_name_list) and (supplied_password in pass_word_list) \
                and user_name_list.index(supplied_username) == pass_word_list.index(supplied_password):
            #Print welcome
            print(f"Correct username and password! Weclome ,{supplied_password}.")
            #if to show different menus
            if supplied_username == 'admin':
                #Return menu for admin 
                return admin(supplied_username)
            else:
                #Return user menu
                return user_menu(supplied_username)

        elif (supplied_username in user_name_list) and (supplied_password in pass_word_list) \
                and user_name_list.index(supplied_username) != pass_word_list.index(supplied_password):
            #Declare validate as false to repeat
            password_validate = False
            #print statement including new line escape commands
            print("Username is Correct! Please Re-enter password: ")

        elif (supplied_username in user_name_list) and (supplied_password not in pass_word_list):
            #Declare validate as false to repeat
            password_validate = False
            #print statement including new line escape commands
            print("Password incorrect. Please Re-enter Password: ")

        elif (supplied_username not in user_name_list) and (supplied_password not in pass_word_list):
            #Declare validate as false to repeat
            password_validate = False
            #print statement including new line escape commands
            print("Password is incorrect. Please Re-enter Password: ")
#closing a file
user_inquiry.close()

#Defining admin option to view menus
def admin(supplied_username):
    #Print statements
    print("Please select from the following options:")
    print("1 - Main Menu")
    print("2 - Admin Menu")
    #Requesting admin input
    admin_choice = int(input(": "))
    #if statement
    if admin_choice == 1:
        #return statement
        return user_menu(supplied_username)
    #else statement
    else:
        #print statement
        print("Admin Menu:")
        #Call admin menu
        return admin_menu(supplied_username)

#Define the admin_menu
def admin_menu(supplied_username):
    #print statements
    print(" 1 - register user \n 2 - add task \n 3 - view all tasks \n 4 - view my tasks \n 5  - Generate Reports \n 6 - Display Statistics \n 7 - exit")
    programme_option = int(input("Please select one of the above options: "))
    #Create nested if to call the defined functions for options
    if programme_option == 1:
        reg_user(supplied_username)
    elif programme_option == 2:
        add_task(supplied_username)
    elif programme_option == 3:
        view_all(supplied_username)
    elif programme_option == 4:
        view_mine(supplied_username)
    elif programme_option == 5:
        gen_reports(supplied_username)
    elif programme_option == 6:
        display_stats(supplied_username)
        #exit option
    elif programme_option == 7:
        print("You have chosen to exit the Task Manager. Thank you!")
        return exit_option(supplied_username)
        #ask for vallid input.
    else:
        #Ask user to input an option
        print("Invalid input! Please select a valid option: ")

#Define the user menu
def user_menu(supplied_username):
    #print statements
    print(" 1 - register user \n 2 - add task \n 3 - view all tasks \n 4 - view my tasks \n 5 - exit")
    programme_option = int(input("Please select one of the above options: "))
    #Create nested if to call the defined functions for options
    if programme_option == 1:
        reg_user(supplied_username)
    elif programme_option == 2:
        add_task(supplied_username)
    elif programme_option == 3:
        view_all(supplied_username)
    elif programme_option == 4:
        view_mine(supplied_username)
    elif programme_option == 5:
        print("You have chosen to exit the Task Manager. Thank you!")
        return exit_option(supplied_username)
        #ask for vallid input.
    else:
        #Ask user to input an option
        print("Invalid input! Please select a valid option: ")
        if supplied_username == "admin":
        	return admin_menu(supplied_username)
        else:
        	return user_menu(supplied_username)

#Define reg_user
user_library = open('user.txt', 'a')

def reg_user(supplied_username):
    print("Register an account here")
    if supplied_username == 'admin':
        new_username = input("Enter Username: ")
        #while loop and in 
        while new_username in user_name_list:
            print("")
            #print statement including a new line escape command
            print(f"The username, {new_username} is already taken .\n"
                  f"Please try another username.")
            new_username = input("Enter Username: ")

        new_password = input("Create Password: ")
        new_password_confirm = input("Confirm Password: ")
        #while loop
        while new_password != new_password_confirm:
            #print statement including a new line escape command
            print("Password's Don't Match.\n"
                  "Please try again:")
            #requesting a users input
            new_password_confirm = input("Confirm Password: ")

        #if statement
        if new_password == new_password_confirm:
            # using the .append() function
            user_name_list.append(new_username)  
            pass_word_list.append(new_password)
            # writing to a file
            user_library.write(f"\n{new_username}, {new_password}") 

        # return statement
        return admin_menu(supplied_username)

    # else statement
    else:
        # print statement
        print("You don't have access to add user")
        # return statement
        return user_menu(supplied_username)

#Define add_task
def add_task(supplied_username):
    print("Add new task here")
    task_username = input("Please enter the username of the person the task is assigned to: ")
    task_title = input("Please enter the title of the task: ")
    task_description = input("Please enter a description of the task: ")
    task_assignment_date = date.today()
    task_due_year = int(input("Please enter the task due Year: "))
    task_due_month = input("Please enter the task due Month: ").capitalize()
    task_due_day = int(input("please enter the task due Day: "))
    #Print statement
    due_date = f"{task_due_day} {task_due_month[0:3]} {task_due_year}"
    #Declaring a variable
    task_complete = "No"

    print("Confirm the above? \n1 - Confirm \n2 - Edit")
    confirmation = int(input("option: "))

    if confirmation == 1:
        #open file
        write_tasks = open("tasks.txt", "a", encoding='utf-8-sig')
        #write to file
        # writing to a file
        write_tasks.write(f"\n{task_username}, {task_title}, {task_description}, "
                                  f"{task_assignment_date.strftime('%d %b %Y')}, {due_date}, {task_complete}")
        # closing a file
        write_tasks.close()
    #else edit
    else:
        print(add_task(supplied_username))

    if supplied_username == "admin":
        return admin_menu(supplied_username)
    else:
        return user_menu(supplied_username)

#Define view_all
def view_all(supplied_username):
	#Opening a file
    tasks_library = open('tasks.txt', 'r', encoding='utf-8')
    #declaring a variable
    task_number = 0
    #for loop and in 
    for task in tasks_library:
        task = task.strip()
        task = task.split(', ')
        #Declaring a variable
        i = 0 

        #for loop and in
        for item in task:
            # if statement
            if i == 0:
                task_number += 1
                #print statement
                print(f"Task Number:		{task_number}")
                print(f"Task Assigned to user:		{item}")
                #Next item
                i += 1
            elif i == 1:
                # print statement
                print(f"Task Title:         {item}")
                #Next item
                i += 1
            elif i == 2:
                print(f"Task Description:   {item}")
                #Next item
                i += 1
            elif i == 3:
                print(f"Time Assigned:      {item}")
                #Next item
                i += 1
            elif i == 4:
                print(f"Task Due Date:      {item}")
                #Next item
                i += 1
            elif i == 5:
                print(f"Task Completion:      {item}")

    # closing a file
    tasks_library.close()
    
    if supplied_username == "admin":
        return admin_menu(supplied_username)
    else:
        return user_menu(supplied_username)

#Define view_mine
def view_mine(supplied_username):
    view_myTask = open("tasks.txt","r")
    #declare variables
    task_available = False 
    x = 0

    for task in view_myTask:
    	task = task.strip()
    	task = task.split(", ")
    	x += 1

    	#
    	#Repeat for each task in file
    	for line in task:
    		#if statement
    		if line in supplied_username:
    			#print statements 
    			print(f"Task Number;		{x}")
    			print(f"Task is Assigned to user;		{task[0]}")
    			print(f"Task Title;		{task[1]}")
    			print(f"Task Description;		{task[2]}")
    			print(f"Task Assignment time;		{task[3]}")
    			print(f"Task Due Date;		{task[4]}")
    			print(f"Task completion;		{task[5]}")

    			task_available = True

    if not task_available:
    	print("No Task available for this user.")

    print("Please select an option below")
    print(" 1 - Edit Task \n 2 - Go Back")
    edit_choice = int(input("Please enter option here: "))

    if edit_choice == 1:
    	#close file 
    	view_myTask.close()
    	#return edit
    	return edit_task(supplied_username)
    else:
        #close file
        view_myTask.close()
        #return menu
        if supplied_username == "admin":
            return admin_menu(supplied_username)
        else:
            return user_menu(supplied_username)

#Define edit_task menu
def edit_task(supplied_username):
    print("Edit task Menu.")
    task_edit_number = int(input("Please enter the task number you want to edit here: "))
    #Open file
    task_to_edit = open("tasks.txt", "r")
    #Using the readlines() function to read the lines of a file
    task_to_edit_read = task_to_edit.readlines()
    check_task = (task_to_edit_read[task_edit_number - 1])
    check_task = check_task.strip()
    check_task = check_task.split(', ')

    #If statement
    if check_task[5] == "No":
        #Print statements including new line escape commands
        print("\nPlease select from the following options:")
        print("1 - Mark Task Complete\n"
              "2 - Edit The Task\n3 - Return")
        #Requesting a users input and converting it into an integer using the int() function
        edit_task_choice = int(input("Choice here: "))
        # if statement
        if edit_task_choice == 1:
            return edit_task_complete(supplied_username, task_edit_number)
        #Elif statement
        elif edit_task_choice == 2:
            return edit_the_task(supplied_username, task_edit_number)

        elif edit_task_choice == 3:
        	if supplied_username == "admin":
        		return admin_menu(supplied_username)
        	else:
        		return user_menu(supplied_username)

    #Else statement
    else:
        #Print statement
        print("This task is already complete and cannot be edited.")
        if supplied_username == "admin":
        	return admin_menu(supplied_username)
        else:
        	return user_menu(supplied_username)

#Define edit_task_complete
def edit_task_complete(supplied_username, task_edit_number):
    #Print statements
    print("")
    print("Mark Task Complete:")
    #Opening a file
    task_to_edit = open('tasks.txt', 'r+')
    task_to_edit_read = task_to_edit.readlines()
    mark_complete = (task_to_edit_read[task_edit_number - 1])
    mark_complete = mark_complete.strip()
    mark_complete = mark_complete.split(', ')

    #if statement
    if mark_complete[5] == 'No':
        #Deleting an item
        mark_complete.__delitem__(5)
        #Declaring a variable
        task_complete = "Yes"
        #Using the .append() function
        mark_complete.append(task_complete)
        #Print statement including a new line escape command
        completed_task = f"{mark_complete[0]}, {mark_complete[1]}, {mark_complete[2]}, {mark_complete[3]}, " \
                         f"{mark_complete[4]}, {mark_complete[5]}\n"
        #Closing a file
        task_to_edit.close()

        #Requesting a users input and converting it into an integer using the int() function
        confirm_change = int(input("1 - Confirm\n"
                                   "2 - Cancel\n"
                                   ": "))

        #If statements
        if confirm_change == 1:
            #Opening a file
            task_to_edit = open('tasks.txt', 'w')
            task_to_edit_read[task_edit_number - 1] = completed_task
            task_to_edit.writelines(task_to_edit_read)
            task_to_edit.close()

        #Else statement
        else:
            #Return statement
            return edit_task_complete(supplied_username, task_edit_number)
        #Print statement
        print("")
        #Print statement
        print("Task Change Complete.")

        if supplied_username == "admin":
        	return admin_menu(supplied_username)
        else:
        	return user_menu(supplied_username)

#Define edit_the_task 
def edit_the_task(supplied_username, task_edit_number):
    #Print statements
    print("")
    print("Edit The Task:")
    print("")
    #Opening a file
    task_to_edit = open('tasks.txt', 'r+')
    task_to_edit_read = task_to_edit.readlines()
    make_change = (task_to_edit_read[task_edit_number - 1])
    make_change = make_change.strip()
    make_change = make_change.split(', ')

    #Requesting a users input and converting it into an integer using the int() function
    change_to_what = int(input("1 - User Assigned:\n"
                               "2 - Due Date:\n"
                               ": "))
    #If statement
    if change_to_what == 1:
        #Deleting an item
        make_change.__delitem__(0)
        #Requesting a users input including a new line escape command
        new_due_date = input("Enter New Assigned Username:\n"
                             ": ")
        #Using the .insert() function
        make_change.insert(0, new_due_date)
        #Print statement including a new line escape command
        completed_task = f"{make_change[0]}, {make_change[1]}, {make_change[2]}, {make_change[3]}, " \
                         f"{make_change[4]}, {make_change[5]}\n"
        #Closing a file
        task_to_edit.close()

        #Requesting a users input and converting it into an integer using the int() function
        confirm_change = int(input("1 - Confirm\n"
                                   "2 - Cancel\n"
                                   ": "))
        #If statement
        if confirm_change == 1:
            #Opening a file
            task_to_edit = open('tasks.txt', 'w')
            task_to_edit_read[task_edit_number - 1] = completed_task
            task_to_edit.writelines(task_to_edit_read)
            # closing a file
            task_to_edit.close()
            # print statement
            print("")
            #Print statement including a new line escape command
            print(f"Task change is complete.\n"
                  f"Task is now assigned to: {new_due_date}.") 
        #Else statement
        else:
            #Return statement
            return edit_the_task(supplied_username, task_edit_number)

    #Elif statement
    elif change_to_what == 2:
        #Deleting an item
        make_change.__delitem__(4)
        #Requesting a users input and converting it into an integer using the int() function
        new_due_year = int(input("Enter Due Date Year: "))
        new_due_month = input("Enter Due Date Month: ").capitalize()
        new_due_day = int(input("Enter Due Date Day: "))

        #Print statement
        new_due_date = f"{new_due_day} {new_due_month[0:3]} {new_due_year}"

        #Using the .insert() function
        make_change.insert(4, new_due_date)
        #Print statement including a new line escape command
        completed_task = f"{make_change[0]}, {make_change[1]}, {make_change[2]}, {make_change[3]}, " \
                         f"{make_change[4]}, {make_change[5]}\n"
        #Closing a file
        task_to_edit.close()
        #Requesting a users input and converting it into an integer using the int() function
        confirm_change = int(input("1 - Confirm\n"
                                   "2 - Cancel\n"
                                   ": "))
        #If statement
        if confirm_change == 1:
            # opening a file
            task_to_edit = open('tasks.txt', 'w')
            task_to_edit_read[task_edit_number - 1] = completed_task
            task_to_edit.writelines(task_to_edit_read)

            # closing a file
            task_to_edit.close()
            # print statements including a new line escape command
            print("")
            print(f"Task change is complete.\n"
                  f"Task is new due date: {new_due_date}.")

            if supplied_username == "admin":
            	return admin_menu(supplied_username)
            else:
            	return user_menu(supplied_username)

#Define gen reports
def gen_reports(supplied_username):
    #Opening files
    task_overview = open('task_overview.txt', 'w+')
    task_count = open('tasks.txt', 'r')

    #Using the readlines() function to read the lines of a file
    task_total = task_count.readlines()
    task_total = len(task_total)

    #Closing a file
    task_count.close()

    #Writing to a file including a new line escape command
    task_overview.write(f"Total Number of Tasks:                          {task_total}.\n")
    #Closing a file
    task_count.close()

    #Opening a file
    task_complete = open('tasks.txt', 'r')
    #Declaring variables
    num_completed = 0
    num_incomplete = 0

    #For loop and in statements
    for task in task_complete:
        task = task.strip()
        task = task.split(', ')

        #For loop and in statement
        for item in task:
            #if and in statement
            if "Yes" in item:
                num_completed += 1
            #if and in statement
            if "No" in item:
                num_incomplete += 1

    #Writing to a file
    task_overview.write(f"Total Number of Completed Tasks:                {num_completed}.\n")
    #Writing to a file
    task_overview.write(f"Total Number of Uncompleted Tasks:              {num_incomplete}.\n")

    #Closing a file
    task_complete.close()

    #Declaring a variable
    num_task_overdue = 0
    #Opening a file
    task_overdue = open('tasks.txt', 'r')
    #For loop and in statement
    for task in task_overdue:
        task = task.strip()
        task = task.split(', ')
        date_today = date.today()
        date_due = datetime.datetime.strptime(task[4], '%d %b %Y')
        date_due = date_due.date()

        #If statement
        if date_due < date_today:
            #If statement
            if task[5] == "No":
                #calculation using the arithmetic operation of addition
                num_task_overdue += 1

    #Writing to a file 
    task_overview.write(f"Total Number of Uncompleted & Overdue Tasks:    {num_task_overdue}.\n")
    incomplete_percent = (num_incomplete / task_total) * 100
    task_overview.write(f"Percentage of Tasks that are incomplete:        {incomplete_percent:.2f}%\n")
    overdue_percent = (num_task_overdue / task_total) * 100
    task_overview.write(f"Percentage of Tasks that are overdue:           {overdue_percent:.2f}%\n")
    #Closing a file
    task_overview.close()

    #Opening a file
    task_overview = open('task_overview.txt', 'r')
    # print statement
    print("Task Overview:")
    print(task_overview.read())
    task_overview.close()

    #Opening a file
    user_overview = open('user_overview.txt', 'w+')
    #writing to a file including a new line escape command
  
    user_overview.write(f"Total Number of Users:                                  {len(user_name_list)}.\n")

    #Opening a file
    task_count = open('tasks.txt', 'r')
    task_total = task_count.readlines()
    task_total = len(task_total)
    
    user_overview.write(f"Total Number of Tasks:                                  {task_total}.\n")
    #Closing a file
    task_count.close()

    #Opening a file
    task_user = open('tasks.txt', 'r')
    #Declaring a variable
    total_task_user = 0

    #for loop and in 
    for task in task_user:
        task = task.strip()
        task = task.split(', ')
        #if statement
        if supplied_username == task[0]:
            total_task_user += 1

    #Writing to a file including a new line escape command
    user_overview.write(f"Total Number of Tasks Assigned to You:                  {total_task_user}.\n")
    #Closing a file
    task_user.close()

    #Opening a file
    task_user = open('tasks.txt', 'r')

    #Declaring  variables
    my_total_task = 0
    task_total = 0
    my_completed = 0
    my_incomplete = 0
    my_over_incomplete = 0

    #for loop and in
    for task in task_user:
        task = task.strip()
        task = task.split(', ')
        task_total += 1
        #if statement
        if supplied_username == task[0]:
            my_total_task += 1
            #if statement
            if task[5] == "Yes":
                my_completed += 1
            #if statement
            if task[5] == "No":
                my_incomplete += 1
                #Declaring variables
                date_due = datetime.datetime.strptime(task[4], '%d %b %Y')
                date_due = date_due.date()
                date_today = date.today()
                #if statement
                if date_due < date_today:
                    my_over_incomplete += 1

   
    percent_my_task = (my_total_task / task_total * 100)
    #Writing to a file including a new line
    user_overview.write(f"Percentage of total tasks assigned to you:              {percent_my_task:.2f} %\n")

    percent_my_completed = (my_completed / task_total * 100)
    #Writing to a file including a new line
    user_overview.write(f"Percentage of total completed tasks assigned to you:    {percent_my_completed:.2f} %\n")
   
    percent_my_incomplete = (my_incomplete / task_total * 100)
    #Writing to a file including a new line escape command
    user_overview.write(f"Percentage of total incomplete tasks assigned to you:   {percent_my_incomplete:.2f} %\n")
   
    percent_incomplete_overdue = (my_over_incomplete / task_total * 100)
    #Writing to a file including a new line escape command
    user_overview.write(f"Percentage of total incomplete tasks assigned to you:   {percent_incomplete_overdue:.2f} %\n")
    # closing files
    task_user.close()
    user_overview.close()

    user_overview = open('user_overview.txt', 'r')
    print("User Overview:")
    print(user_overview.read())
    user_overview.close()

    if supplied_username == "admin":
        return admin_menu(supplied_username)
    else:
        return user_menu(supplied_username)

#Define display_stats
def display_stats(supplied_username):
    print("Display Statistics")
    #Opening files
    task_overview = open("task_overview.txt", "r")
    user_overview = open("user_overview.txt", "r")
    #Ff statement and an 'and' and a 'not' statement
    if task_overview and not task_overview:
        print("Reports Have Not Been Generated.")
        return admin_menu(supplied_username)

    print("Task Overview:")
    print("")

    #for loop and in statements
    for report in task_overview:
        # using the .strip() function
        report = report.strip()
        # print statement
        print(report)

    #Closing a file
    task_overview.close()
   
    print("")
    print("")

    print("User Overview:")
    print("")

    #for loop and in
    for report in user_overview:
        report = report.strip()
        #Print statement
        print(report) 
        return admin(supplied_username) 

# creating a function
def exit_option(supplied_username):
   
    print("Confirm exit? \n 1 - Confirm \n 2 - Cancel")
    # requesting a users input and converting it into an integer using the int() function
    exit_confirm = int(input("Option here: "))
    #if statement
    if exit_confirm == 1:
        # print statement
        print(f"Goodbye {supplied_username}.")
        # eturn statement
        return exit(0)
    # else statement
    else:
        # print statement
        print(f"Welcome Back, {supplied_username}")
        #if
        if supplied_username == "admin":
        	return admin_menu(supplied_username)
        else:
        	return user_menu(supplied_username)

#
#Programme starts here 
#

#Print text to present program: 
print("This is the Task manager Program \nWelcome!")
print(login())

