# # loops
# # Write a Python program that prints all even numbers between 1 and 20 using a for loop.
for num in range(2,21,2):
    print(num)

# # Use a while loop to ask the user to input a number until
# #  they provide a number greater than 10.
num=0
while num <= 10:
    num=int(input("enter the number greater than 10: "))
    if num <= 10:
        print("the number is not greater than 10.")

# : Write a program that prints the multiplication table (from 1 to 10)
#  for numbers from 1 to 5 using nested for loops.
for x in range(1,6):
    print(f"multiplication table for {x}")
    for n in range(1,11):
        print(f"{x} * {n} = {x * n}")
        print()
# # : Given a list of integers, [4, 7, 2, 9, 12, 15], write a program using 
# a for loop to find the sum of all odd numbers and print the result.
integers = [4, 7, 2, 9, 12, 15]
odd_sum = 0
for num in integers:
    if num % 2 != 0:
        odd_sum += num
print("Sum of odd numbers:", odd_sum)

# lists
#Create a list of 5 fruits and print each fruit on a new line using a for loop.
fruits = ("apples", "oranges", "mangoes", "pears","jackfruit")
for x in fruits:
    print(x)

# Write a function that takes a list of numbers and returns a new list with each number
#  squared. Example: [1, 2, 3] should become [1, 4, 9].
def squared_number(numbers):
    return[number **2 for number in numbers]
numbers = [1,2,3]
square_numbers = squared_number(numbers)
print(square_numbers)


# Write a Python program that takes two lists, list1 = [1, 2, 3] and list2 = [4, 5, 6],
#  and combines them into a single list, combined = [1, 4, 2, 5, 3, 6].
list1 =[1,2,3]
list2 =[4,5,6]
list3 = list1 + list2
print(list3)

#Given a list of numbers, [3, 1, 4, 1, 5, 9, 2], write a program to find 
# and print the two largest numbers in the list without using the max() function.
numbers = [3,1,4,1,5,9,2]
numbers.sort(reverse=True)
largest = numbers[0]
second_largest = numbers[1]
print(numbers)
print("The largest number is", largest)
print("The second largest number is", second_largest)

# dictionaries
# Create a dictionary with three key-value pairs representing a student's information:
#  name, age, and grade. Print each key-value pair on a new line.
students_info = {
    "name": "faith",
    "age": 20,
    "grade": "cohort 4"
}
for keys,value in students_info.items():
    print(keys + ":",value)

# Write a function that takes a dictionary of people's names and their ages,
#  {'Alice': 24, 'Bob': 19, 'Charlie': 30}, and returns a list of names of people who are 21 or older.
def filter_adults(people):
    return[name for name, age in people.items() if age >= 21]
people = {"Alice": 24, "Bob": 19, "Charlie": 30}
adults =filter_adults(people)
print(adults)

#Given a dictionary representing items in a store with their prices, 
#{'apple': 0.5, 'banana': 0.3, 'orange': 0.7}, write a program that
#  takes a list of items bought, ['apple', 'orange', 'banana', 'banana'],
#  and calculates the total cost.
def total_cost():
    store_dict = {
        "apple":0.5,
        "banana":0.3,
        "orange":0.7
    }
    items_bought = {"apple","banana","orange","banana"}
    total_cost=0
    for items in items_bought:
        total_cost+= store_dict[items]
        print("the total cost of items is: ", total_cost)
    total_cost()

#Write a program that counts the occurrences of each word in a given sentence.
#  Example: for the sentence "hello world hello," the output should be
#  {'hello': 2, 'world': 1}.
def word_occurence():
    sentence = "hello world hello"
    words = sentence.split()
    occurences = {}
    for word in words:
        if word in occurences:
            occurences[word] += 1
        else:
                occurences[word] = 1
    print(occurences)
    word_occurence()

# oop
# Create a class called Car with attributes brand and color. Instantiate an
#  object of the Car class and print its attributes.
class car:
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color

    def start_engine(self):
            print(f"the engine of the {self.color} {self.brand} has started.")

my_car = car("mercedes", "black")
print(f"brand: {my_car.brand}")
print(f"color: {my_car.color}")
my_car.start_engine()

#Add a method called start_engine to the Car class that prints a
#  message saying the engine of the car has started. Create an
#  instance of Car and call the method.
class car:
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color

    def start_engine(self):
            print(f"the engine of the {self.color} {self.brand} has started.")
my_car.start_engine()

# Create a class called BankAccount with attributes account_number and balance. Add methods to:
#Deposit an amount.
#Withdraw an amount (only if sufficient balance exists).
#Print the account balance.
class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        print(f"Deposited ${amount:.2f} to account {self.account_number}. New balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print(f"Insufficient balance to withdraw ${amount:.2f} from account {self.account_number}.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f} from account {self.account_number}. New balance: ${self.balance:.2f}")

    def print_balance(self):
        print(f"Account {self.account_number} balance: ${self.balance:.2f}")

account = BankAccount("12345678", initial_balance=2000)
account.deposit(2000)
account.print_balance()
account.withdraw(2000)
account.print_balance()
account.withdraw(1000)
account.print_balance()
account.deposit(0)
account.withdraw(700)

#: Implement a class called Library that manages a collection of books.
#  Each book has a title, author, and available status. The Library class should have methods to:
#Add a book to the library.
#Remove a book from the library.
#Check if a book is available by title.
#Borrow a book (fmark it as unavailable if it’s available).
#Return a book (mark it as available again if it was borrowed).
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def _str_(self):
        return f"'{self.title}' by {self.author} ({'Available' if self.is_available else 'Unavailable'})"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)
        print(f"Book '{title}' by {author} added to the library.")

    def remove_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print(f"Book '{title}' removed from the library.")
                return
        print(f"Book '{title}' not found in the library.")

    def check_availability(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book.is_available
        print(f"Book '{title}' not found in the library.")
        return False

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.is_available:
                    book.is_available = False
                    print(f"You have borrowed '{title}'.")
                else:
                    print(f"Book '{title}' is currently unavailable.")
                return
        print(f"Book '{title}' not found in the library.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if not book.is_available:
                    book.is_available = True
                    print(f"Book '{title}' has been returned.")
                else:
                    print(f"Book '{title}' was not borrowed.")
                return
        print(f"Book '{title}' not found in the library.")

    def list_books(self):
        if not self.books:
            print("The library is empty.")
        else:
            for book in self.books:
                print(book)

library = Library()
library.add_book("To Kill a Mockingbird", "Harper Lee")
library.add_book("1984", "George Orwell")

print("\n")

library.check_availability("1984")
library.borrow_book("1984")
library.check_availability("1984")
library.return_book("1984")
library.remove_book("To Kill a Mockingbird")
library.list_books()


