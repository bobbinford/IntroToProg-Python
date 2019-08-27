#-------------------------------------------------#
# Title: Working with Dictionaries
# Dev:   RRoot
# Date:  July 16, 2012
# ChangeLog: (Who, When, What)
#   Bob Binford, 08/26/2019, added exception and pickling to code
#-------------------------------------------------#

# Step 1 - Load data from a file
    # When the program starts, load each "row" of data 
    # in "ToDo.txt" into a python Dictionary.
    # Add the each dictionary "row" to a python list "table"

import pickle
objFileName = "Todo.txt"

dictionary = {}
try:
    with open(objFileName, "r") as file:
        for line in file:
            key, value = line.strip().split(",")
            dictionary[key] = value
except IOError:  # provide an error message to the user if there is no todo txt file
    print("File not found")

class Add_Remove(object):  # created class of add or remove items
    def add_item():  # this was previously embedded in the elif statement below
        number = int(input('How many tasks would you like to add?'))
        for x in range(number):
            task = input('Enter task:')
            prior = input('Enter priority:')
            dictA = {task: prior}
            dictionary.update(dictA)
        print("Updated To Do List:", dictionary)

    def rem_item():
        number = int(input('How many tasks would you like to remove?'))
        for x in range(number):
            dictionary.pop(input('Enter task to remove:'), )
        print("Updated To Do List:", dictionary)


def save_to_file():
    todo_file = open(objFileName, "wb")
    pickle.dump(dictionary, todo_file)  # data saved to text file via pickling, not readable to user
    todo_file.close()
    print('Data added to table successfully!')
    pickle_in = open(objFileName,'rb') # ensure pickled list is readable via program
    example_dict = pickle.load(pickle_in)
    print('Here is your list:')
    print(example_dict)
    pickle_in.close()



# Step 2 - Display a menu of choices to the user
while(True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 4] - "))
    print()#adding a new line

    # Step 3 -Show the current items in the table
    if strChoice.strip() == '1':
        print(dictionary)
        continue
    # Step 4 - Add a new item to the list/Table
    elif strChoice.strip() == '2':
        Add_Remove.add_item()
        continue
    # Step 5 - Remove a new item to the list/Table
    elif strChoice == '3':
        Add_Remove.rem_item()
        continue
    # Step 6 - Save tasks to the ToDo.txt file
    elif strChoice == '4':
        save_to_file()
        continue
    elif strChoice == '5':
        break #and Exit the program

