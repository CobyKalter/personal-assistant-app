class PersonalAssistant:

  def __init__(self, todos, birthdays, contacts):
    self.todos = todos
    self.birthdays = birthdays
    self.contacts = contacts
    
# Todo functions
  def add_todo(self, new_item):
    self.todos.append(new_item)

  def remove_todo(self, todo_item):
    if todo_item in self.todos:
      # Get the todo_item index in list
      index = self.todos.index(todo_item)
      # pop the index for todo_item in todos list
      self.todos.pop(index)
    else:
      print("Todo is not in list!")

  def get_todos(self):
    return self.todos
    
# Birthday Functions
  def get_birthdays(self):
    return self.birthdays
  
  def get_birthday(self, name):
    if name in self.birthdays:
      print(f"{name}'s birthday is on {self.birthdays[name]}.")
    else:
      print("Can't find a birthday for that person")

  def add_birthday(self, name, date):
    if name in self.birthdays:
      print("That person already has a birthday in the system!")
    else:
      self.birthdays[name] = date
      print(f"Added {name}'s birthday to the system!")

  def remove_birthday(self, name):
    if name in self.birthdays:
      self.birthdays.pop(name)
      print(f"{name}'s birthday has been removed.")
    else:
      print("That birthday cannot be removed.")

 # Contact Functions 

  def get_contacts(self):
    return self.contacts
  
  def get_contact(self, name):
    if name in self.contacts:
        print(f"{name}'s profession is {self.contacts[name]}.")
    else:
        return "No contact with that name!"

  def add_contact(self, name, profession):
    if name in self.contacts:
      print("That contact already exists!")
    else:
      self.contacts[name] = profession
      print(f"Added {name} to contacts!")

  def remove_contact(self, name):
    if name in self.contacts:
      self.contacts.pop(name)
      print(f"{name} has been removed from contacts!")
    else:
      print("That contact cannot be removed!")

# Code to test the class
  # assistant = PersonalAssistant()
  # print(assistant.get_contact("Chelsea"))
  
  # assistant.add_todo("Pick up groceries")
  # assistant.add_todo("Run errands")
  # print(assistant.get_todos())
  # print(assistant.get_birthday("Cory"))