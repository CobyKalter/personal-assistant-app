import json

#imports PersonalAssistant.py file
from PersonalAssistant import PersonalAssistant

#ADD CODE: open JSON file and pass data to PersonalAssistant class
with open('todo.json', 'r') as todos, open('birthdays.json','r') as birthdays, open('contacts.json', 'r') as contacts:
  todo_list = json.load(todos)
  birthday_list = json.load(birthdays)
  contact_list = json.load(contacts)
  assistant = PersonalAssistant(todo_list, birthday_list, contact_list)


done = False

while not done:
    user_command = input(
        """
How can I help you?

    **** To-dos *****
    1: Add a to-do
    2: Remove a to-do
    3: Get to-do list
    **** Birthdays ****
    4: Get Birthday
    5: Add Birthday
    6: Remove Birthday
    **** Contacts ****
    7: Get Contacts
    8: Add Contact
    9: Remove Contact

    Select a number or type 'Exit' to quit: 
    
    """
    )
    # Add Todo
    if user_command == "1":
        user_input = input("Item to add to to-do list: ")
        assistant.add_todo(user_input)
    # Remove Todo
    elif user_command == "2":
        print(f"Your current todos: {assistant.get_todos()}")
        user_input = input("Item to remove from to-do list: ")
        print(f"\n {assistant.remove_todo(user_input)}")
    # Get Todos
    elif user_command == "3":
        print("\nYour to-do list")
        for todo in todo_list:
            print(todo)
    # Get Birthday  
    elif user_command == "4":
        print("\nYour Birthday List: \n")
        for name in birthday_list:
          print(name)
        name_input = input("Please enter a name for a birthday: ")
        print(assistant.get_birthday(name_input))
    # Add Birthday  
    elif user_command == "5":
          name = input("Name of the person: ")
          birthday = input("Their birthday (ex: 08/18/2000): ")
          print(assistant.add_birthday(name, birthday))
    # Remove Birthday 
    elif user_command == "6": 
          print(assistant.birthdays)
          name = input("Which name would you like to remove? ")
          print(assistant.remove_birthday(name))
    # Get Contacts
    elif user_command == "7":
        print("\nYour Contact List: \n")
        for name in contact_list:
            print(name)
        name_input = input("Please enter a name for a contact: ")
        print(assistant.get_contact(name_input))
    # Add Contact
    elif user_command == "8":
          name = input("Name of the person: ")
          profession = input("What is their profession?: ")
          print(assistant.add_contact(name, profession))
    # Remove Contact
    elif user_command == "9":
          print(assistant.contacts)
          name = input("Which name would you like to remove? ")
          print(assistant.remove_contact(name))
    # Exit
    elif user_command == "exit" or user_command == "Exit" or user_command == "EXIT":
        done = True
        print("\nGoodbye, see you soon!")
    else:
        print("\nNot a valid command.")

# ADD CODE: write data to JSON file
with open("todo.json", "w") as write_todos, open("birthdays.json", "w") as write_birthdays, open("contacts.json", "w") as write_contacts:
  json.dump(assistant.get_todos(), write_todos)
  json.dump(assistant.get_birthdays(), write_birthdays)
  json.dump(assistant.get_contacts(), write_contacts)