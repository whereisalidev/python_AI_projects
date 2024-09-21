#Python: Basics

print("Hello World!")

#----------------------------------------------------------------------------------------------------------

#Addition, subtraction, multiplication, and division of two numbers input by the user.
try:
    x = int(input("Enter number 1: "))
    y = int(input("Enter number 2: "))
    print(f"Addition: {x+y}\nSubtraction: {x-y}\nMultiplication: {x*y}\nDivision: {x/y}")
except ValueError:
    print("Invalid input!")
except ZeroDivisionError:
    print("Divided by zero is not allowed!")

#----------------------------------------------------------------------------------------------------------

#Program to generate and print a random number between a specified range.
import random

start = 1
end = 50
x = random.randint(start, end)
print("Random Number b/w %s & %s is %s" %(start, end, x))


# --------------------------------------------------Python:Projects---------------------------------------------------------------


# Automated Teller Machine (ATM) Python console project:
def function(choice, balance):
    if choice == '1':
        amount = float(input("Enter Amount: "))
        if amount > 0:
            balance += amount
        else:
            print('Invalid amount!!')
    elif choice == '2':
        amount = float(input("Enter Amount: "))
        if amount > 0:
            if balance >= amount:
                balance -= amount
            else:
                print('Insufficient balance')
        else:
            print('Invalid amount!!')
    elif choice == '3':
        print("Balance: " + str(balance))
    else:
        print("Invalid Choice!")

    return balance

balance = 0.0

while True:
    print('----------------------------------')
    print('| Automated Teller Machine (ATM) |')
    print('----------------------------------')
    
    print("1) Deposit Money")
    print("2) Withdraw Money")
    print("3) Show Balance")
    print("4) Quit")
    
    choice = input('Enter choice: ').strip()
    
    if choice == '4':
        break
    
    balance = function(choice, balance)

#----------------------------------------------------------------------------------------------------------

#Todo_List_Python:
class ToDoList:
    def __init__(self, taskList=None):
        if taskList is None:
            taskList = []
        self.taskList = taskList
    
    def add_task(self, task):
        self.taskList.append(task)
        print(f'Task "{task}" added.')

    def view_tasks(self):
        if not self.taskList:
            print('No tasks to display.')
        else:
            print('Tasks:')
            for i, task in enumerate(self.taskList, start=1):
                print(f'{i}. {task}')

    def del_task(self, task_index):
        if 0 <= task_index < len(self.taskList):
            removed_task = self.taskList.pop(task_index)
            print(f'Task "{removed_task}" deleted.')
        else:
            print('Invalid task number.')

def main():
    taskList = []
    obj = ToDoList(taskList=taskList)

    while True:
        print('\nTo-Do List:')
        print('1) Add Task')
        print('2) View Tasks')
        print('3) Delete Task')
        print('4) Quit')
        
        choice = input('Enter your choice: ').strip()
        
        if choice == '1':
            task = input('Enter task: ').strip()
            obj.add_task(task)
        elif choice == '2':
            obj.view_tasks()
        elif choice == '3':
            obj.view_tasks()
            if taskList:
                try:
                    task_index = int(input('Enter task number to delete: ')) - 1
                    obj.del_task(task_index)
                except ValueError:
                    print('Invalid input! Please enter a number.')
        elif choice == '4':
            break
        else:
            print('Invalid choice! Please try again.')

if __name__ == '__main__':
    main()

# -----------------------------------------------------------------------------------------------------------------


# Python : Library Management System:
class Book:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available

    def __str__(self):
        return f"Book Details:\nTitle: {self.title}\nAuthor: {self.author}\nAvailability: {self.available}\n"
    

class Library:
    def __init__(self, bookList=[]):
        self.bookList = bookList
        

    def add_book(self, book:Book):
        self.bookList.append(book) 
        

    def view_books(self, viewAllBooks=True, title=None):
        if viewAllBooks==True:
            for book in self.bookList:
                print(book)
        else:
            for book in self.bookList:
                if book.title == title.strip():
                    print(book)
                    return
            print(f'Book {title} Not Found!!')

    def delete_book(self, title):
        for book in self.bookList:
            if book.title == title.strip():
                self.bookList.remove(book)
                print(f'Book "{title.strip()}" deleted!')
                return
            print('Book not Found!!')

    def search_book(self, title):
        self.view_books(viewAllBooks=False, title=title)



lib = Library()
lib.add_book(Book(title='Goals', author='Brian Tracy'))
lib.add_book(Book(title='How to Win Friends & Influence people', author='Dale Carnegie'))
lib.search_book(title='Goals')
lib.delete_book(title='Goals')
lib.view_books()
















