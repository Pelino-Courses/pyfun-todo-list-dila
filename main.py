import todolist

# This is a main function.
def main(): 
    # The program creates the list to store tasks for the to do.
    todotasks = []
    print('Welcome to our program\n')
    # This loop runs indefinitely unless stopped.
    while True:
        print('Choose what you want to do\n')
        # This is the menu list for the user to choose from.
        print('\t1. Add a task\n\t2. Mark as complete\n\t3. View list\n\t4. Remove a task\n\t5. Exit')
        choice = int(input())
        # This checks the user input.
        if choice == 1:
            # This take user input and call function to add the task specified
            taskname = str(input('Enter your task: '))
            todolist.add_task(taskname, todotasks)
        elif choice == 2:
            taskname = int(input('Enter the task ID: '))
            todolist.mark_completed(taskname, todotasks)
        elif choice == 3:
            todolist.view_list(todotasks)
        elif choice == 4:
            taskid = int(input('Enter the task ID: '))
            todolist.remove_task(taskid, todotasks)
        elif choice == 5:
            # If the user chooses exit, the program terminates.
            print("Thank you for using our program! See you next time!")
            break
        # If none of the above conditions are met, the user gets the message
        else:
            print('There is no such choice. Please try again!')

if __name__ =='__main__':
    main()



