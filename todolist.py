# This is a function to add a task in the to do list.
def add_task(taskname, list):
    new_id = len(list) + 1
    # This adds the dictionary containing id, taskname and status to the to do list.
    list.append({'id': new_id, 'task': taskname, 'status': 'Not completed'})
    print(f'{taskname} is inserted successfully')

# This is a function for marking a task as complete
def mark_completed(id, list):
    # This loop is used to iterate in the list and find the id specified then updates the status to Completed.
    for task in list:
        if task['id'] == id:
            print(task['id'], id)
            task.update({'id':id,'task':task['task'],'status':'Completed'})
    print(f'Task marked as complete ')

# This function prints all activities in the to do 
def view_list(list):
    # The function first checks if there are some activities in the to do list and if there are none it prints a message for the user.
    if len(list) == 0:
        print('You have no activities in your todo') 
    else: 
        print('Tasks in the list \n')
        list.sort(key=lambda x: x.get('status'),reverse = True)
        print('ID\t TASK\t STATUS\n')
        # This loops in the to do list and prints the elements
        for task in list:
            print(task['id'],'\t', task['task'],'\t', task['status'])
        print('\n')

# This function is for deleting a task from the to-do list.
def remove_task(id,lis):
    # First, we search for the element with id given by the user and store the result in a list.
    res = list(filter(lambda task: task['id'] == id, lis))
    lis.remove(res[0])
    print(f'Task removed successfully')
    nbr = 0
    # This loop assigns new IDs to the tasks after one is deleted.
    for task in lis:
        task['id']= nbr+1
        nbr+=1
    

    