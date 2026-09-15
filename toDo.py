import os # used for clearing the terminal screen so can have more of an app feel
import subprocess # used as part of clearing the terminal screen

task_list = []
menu = {1:"1. Add tasks", 2: "2. View tasks", 3: "3. Delete tasks", 4: "4. Quit the application"}
count = None

# displays the menu selections
def display_menu():
    """Prints the main menu options to the terminal."""
    print("                    ")
    print("═" * 15)
    print("   MAIN MENU   ")
    print("═" * 15)
    print("                    ")
    
    for key, value in menu.items():
        print(value)

# takes the user menu selection and checks if it is an integer and a valid selection in the menu - probably could refactor to make these checks a re-usable function for other parts of code
def valid_input(check_input):
    """Checks user menu input for errors"""
    
    try:
        # Step 1: Convert to integer, raise ValueError if not int
        menu_check = int(check_input)
        
        # Step 2: Check if existing menu item, could raise KeyError if not part of menu dictionary
        menu[menu_check]

    except ValueError:
        clear_screen()
        print(" " * 15)
        print(f"\033[1m\033[48;5;208m\033[30mError: User input of '{check_input}' is not an integer. Please make a valid menu selection via the associated menu item number.\033[0m")
        
    except KeyError:
        clear_screen()
        print(" " * 15)
        print(f"\033[1m\033[48;5;208m\033[30mError: User input of '{menu_check}' is not a valid menu selection. Please make a valid menu selection from menu item numbers 1-4.\033[0m")      
    
    else:
        clear_screen()
        print(f"You made menu selection: {menu[menu_check]}")
        return menu_check
    
    finally:
            print("-" * 15)
    
#checks exit selction and confirms if want to exit the program
def exit_selection(keep_loop_running): 
    """Creates a Y and N menu confirming the users intent to exit the program. Seeks to avoid fatfingers ruining user experience."""
    while keep_loop_running != 0:
        
        confirm_exit = input("\033[1;97;41mConfirm you want to exit the program. Enter 'Y' for Yes and 'N' for No.\033[0m").lower()# takes input and converts to lower case so control flow not case sensitive
        
        if not confirm_exit.isalpha(): # checks if is a letter vs a number in the string input received and generates error message if not a letter input
            clear_screen()
            print(f"\033[1m\033[48;5;208m\033[30mError: User input of '{confirm_exit}' is not a letter. Please enter 'Y' to exit or 'N' to not exit the program.\033[0m")
            print("\n--------------------\n")
        else:
            if confirm_exit == "y": # exits program if input is y or Y
                keep_loop_running = 0
                close_program()
            elif confirm_exit == "n": # goes back to main menu if input is n or N
                keep_loop_running = 0
                clear_screen() 
            else: # if not letter y or n generates error message asking for correct input
                clear_screen()
                print(f"\033[1m\033[48;5;208m\033[30mError: User input of '{confirm_exit}' is not an available choice. Please enter 'Y' to exit or 'N' to not exit the program.\033[0m")
                print("\n--------------------\n")

#Function prompting user to enter a task, handling input errors, and will return a task variable that is appended to the task_list list in the function user_prompt
def add_task():
    """Prompts user for task input and returns that task to append to a task_list list variable."""
    
    latest_task = (input("Enter a task to add to your task list:"))
    
    # checks if the entry is a blank string
    if not latest_task:
        clear_screen()
        print(f"\033[1m\033[48;5;208m\033[30mError: You did not enter a task. Your entry of '{latest_task}' is blank. Please add a task.\033[0m")
        print("--------------------")
        return
    elif latest_task.isspace():# check if the entry is only blank space
        clear_screen()
        print(f"\033[1m\033[48;5;208m\033[30mError: You did not enter a task. Your entry of '{latest_task}' is a blank space. Please add a task.\033[0m")
        print("--------------------")
        return
    elif len(latest_task) > 250:# checks if the entry is over 250 character limit
        clear_screen()
        print(f"\033[1m\033[48;5;208m\033[30mError: The task is over the limit of 250 characters. Please adjust the task character length.\033[0m")
        print("--------------------")
        return
    else:# returns the task if it is populated with characters that are not spaces
        clear_screen()
        print(f"The task: '{latest_task}' has been added to your list")
        print("--------------------")  
        return latest_task

def delete_task(task_list): 
    """Shows the user the list of tasks available for deletion and prompts the user to delete a task via integer selection. It then removes the task from the task_list."""
     # This try except block is to check if the task list is empty
    try:

        test_if_populated = task_list[0]
        
    except IndexError:
        print("\033[1m\033[48;5;208m\033[30mError: The task list is empty! There are no tasks to delete.\033[0m")
        return
    
    else:
        keep_loop_running = 1
    
    # This loop is for task deletion and handling user input errors
    while keep_loop_running != 0:
        
        print("                    ")
        print("─" * 30)
        print("TASKS AVAILABLE FOR DELETION")
        print("─" * 30)
        print("                    ")
        for number, task in enumerate(task_list, start=1):
            print(f"{number}: {task}")
        print("                    ")        
        
        # This try except block captures errors related to index value and ValueError    
        try:
        
            delete_input = input("Enter a task number to delete from the task list:")
            
            # checks if a user enters a value less than 1 this produces an error message and prevents the index value of the deleted task index from being below 1 and causing incorrect task deletion
            if int(delete_input) > 0:
                deleted_task_index = int(delete_input) - 1
                
                deleted_task = task_list[deleted_task_index]
                del task_list[deleted_task_index]
                clear_screen()
                
                print(f"The task: '{deleted_task}' has been deleted from the task list")
                print("--------------------")
                keep_loop_running = 0
                return task_list
                
            else:
                clear_screen()
                print("\033[1m\033[48;5;208m\033[30mError: There are no tasks listed with a number of 0 or less! Please choose a numbered task to delete.\033[0m")
                print("--------------------")
        
        except IndexError:
            clear_screen()
            print(f"\033[1m\033[48;5;208m\033[30mError: The user input of '{delete_input}' is not an available choice. Please select the number of an available task to delete.\033[0m")
            print("--------------------")
            
        except ValueError:
            clear_screen()
            print(f"\033[1m\033[48;5;208m\033[30mError: User input of '{delete_input}' is not an integer. Please make a valid menu selection via the associated menu item number.\033[0m")
            print("--------------------")
        
def view_task(task_list):
    """Displays an ordered list of all current tasks that have been input. Shows an error if the task_list is empty."""
    
     # checking if list has any value then iterating over list to display alongside index+1 #
     
    try:
        first_item = task_list[0]
        print("                    ")
        print("─" * 15)
        print("   TASK LIST   ")
        print("─" * 15)
        for number, task in enumerate(task_list, start=1):
            print(f"{number}: {task}")
            
    except IndexError:
        print("\033[1m\033[48;5;208m\033[30mError: The task list is empty! Please add a task to view.\033[0m")

# function to clear the terminal and close the program letting the user know they have exited the program
def close_program():
    """Displays an exit message to confirm that the user has exited the program."""
    
    subprocess.run('cls' if os.name =='nt' else 'clear', shell=True) # clears screen before exit message
    print("--------------------")  
    print("\n Exiting program...\n    Good Bye\n")
    print("--------------------\n")  
    exit(0)
        
#function that takes in the user menu input and directs it to the appropriate menu function
def user_prompt(user_menu_selection): 
    """Routes user main menu input to error checking. If no errors continues routing to display appropriate menu function data and prompts."""
    
    #checks input value is correct type and in parameters. If so then allows user to navigate menu or returns error message.
    if (selection := valid_input(user_menu_selection)):
        if selection == 1:
            check_task = add_task()
            if check_task is not None: # Was using function add_task() in append but a blank return, returned "None" which was then added to task_list list
                task_list.append(check_task)
        elif selection == 2:
            view_task(task_list)
        elif selection == 3:
            delete_task(task_list)
        elif selection == 4:
            return exit_selection(selection)
        
def display_welcome_msg(count):
    """Function that displays a one time welcome message when the user first loads the program."""
    if not count:
        clear_screen()
        print("   WELCOME TO TASKER   \n \033[3mWhere you run your day!\033[0m")
        
def clear_screen():
    """Clears the terminal for user accessibility and aesthetics of the program"""
    subprocess.run('cls' if os.name =='nt' else 'clear', shell=True)
    

# Loop that runs until user chooses to exit the program via menu or Ctrl + C
while True:    
    try:
        display_welcome_msg(count)  
        display_menu()
        user_prompt(input(f"\033[48;5;22;97mMake your number selection:\033[0m"))
        count = 1
        
    #if user enters Ctrl + C to manually exit the program rather than getting extra message looks cleaner
    except KeyboardInterrupt:
        close_program()

     


    