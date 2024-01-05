#libary management system
import time

print("\n\n\t\twelcome to abc libary \n\t\t\tNaikap,ktm")

def books_store():
    books = {
    "Fantasy": [
        {"title": "harry potter and the sorcerer's stone", "price": 15.99, "author": "J.K. Rowling", "edition": "1st", "quantity": 50},
        {"title": "the hobbit", "price": 12.99, "author": "J.R.R. Tolkien", "edition": "2nd", "quantity": 30},
    ],
    "Mystery": [
        {"title": "the da vinci Code", "price": 18.99, "author": "Dan Brown", "edition": "3rd", "quantity": 25},
        {"title": "gone girl", "price": 14.99, "author": "Gillian Flynn", "edition": "1st", "quantity": 40},
    ],
    "Science Fiction": [
        {"title": "dune", "price": 21.99, "author": "Frank Herbert", "edition": "4th", "quantity": 20},
        {"title": "ender's game", "price": 16.99, "author": "Orson Scott Card", "edition": "2nd", "quantity": 35},
    ],
            }
    total_price=0
    price=0
    exit=False
    while exit !=True:
        
        genre = input("Enter the genre (Fantasy, Mystery, Science Fiction): ").capitalize()
        if genre in books:
            available_titles = [book["title"] for book in books[genre]]
            print(f"\nAvailable Titles in {genre}:")
            for title in available_titles:
                print(f"- {title}")
        else:
            print("Invalid genre.")
            
        title = input("Enter the title of the book you want to buy: ").lower()

        if genre in books and any(book["title"] == title for book in books[genre]):
            book_details = next(book for book in books[genre] if book["title"] == title)
            print("\nBook Found! Details:")
            print(f"Title: {book_details['title']}")
            print(f"Author: {book_details['author']}")
            print(f"Edition: {book_details['edition']}")
            price=book_details['price']
            print(f"Price: ${book_details['price']}")
            total_price=total_price+price
            print(f"Available Quantity: {book_details['quantity']}")

            exit=input("\n Press e to exit and c to continue to choce other books:\t>").lower()
            if exit == 'e':
                exit =True
                total_price=total_price
                print(f'Your total price is ${total_price}')
            else:
                exit= False
        else:
            print("Book not found.")
    
      
def new_mem():
    error = False
    while error !=True:  
        try:
            detail = {
                    "Name": input("Enter name :").lower(),
                    "Contact": input("Enter contact no.:"),
                    "Address": input("Enter address :"),
                    "Email": input("Enter email id :")
                    }
            error = True
        except ValueError:
                print("Invalid input error!! Please fill data carefully.")
                error = True
    
    def write_to_file(detail, record_file):
        with open(record_file, 'a') as file:
                
            file.write(f"Name: {detail['Name']}\n")
            file.write(f"Contact: {detail['Contact']}\n")
            file.write(f"Address: {detail['Address']}\n")
            file.write(f"Email: {detail['Email']}\n\n")
            
    write_to_file(detail, "record.txt")
    print('\nRecord saved successfully!')
    books()
        
def old_mem():
    mem_name = input("Enter your name: ").lower()
    found = False
    record = {}

    with open("record.txt", "r") as file:
        lines = file.readlines()
    
    for line in lines:
        if mem_name in line:
            found = True
            print("Record Found!")
            print("---------------------------")
            print(line)
            break

    if not found:
        print("Record not found for ID:", mem_name)
        print("pleasse resustar name first!!")
        new_mem()
        
def employee():
    at=0
    attempt=False
    while attempt==False:
        emp_name = input("Enter your name: ")
        found = False
        record = {}

        with open("employee.txt", "r") as file:
            lines = file.readlines()
        
        for line in lines:
            if emp_name in line:
                found = True
                print("Record Found!")
                print("---------------------------")
                print(line)
                print("welcome to Abc library store. Now get back to work ")
                break

            else:
                print("Record not found for ID:", emp_name)
                at+=1
                attempt =False
                if at==2:
                    attempt =True
                    print("You are not allowed to login !!!")

def visitor_details():
    x=open("record.txt", "r")
    for i in x:
        print(i)      
        
def employee_details():
    edit=input("Select option\n1. Add employee data\n2. View emplyee record.")
    if edit==1:
        details={"Name":input("Enter name :"),
                 "Education":input("Enter your education :"),
                 "Experiences":input("Enter your experiences :"),
                 "issued_date":time.asctime(time.localtime(time.time()))}
        with open("employeee.txt",'a+') as f:
            f.write("\n"+str(details))
    elif edit==2:
        x=open("employee.txt", "r")
        for i in x:
            print(i)  
         
def owner():
    own_password=input("Enter a password: ")  
    if own_password=='my_shop':
        monitor=input("Select option:\n1>Data of employee\n2>Data of visitor\n>") 
        if monitor==2:
            visitor_details()
        else:
            employee_details()

def display():
    position=int(input("\nSelect option:\n1.New visitor\n2.Old visitor\n3.other\n>>"))

    if position==1:
        new_mem()
        print("\n")
        books_store()
        
                
    elif position==2:
        old_mem()
        books_store()
        

    elif position == 3:
        role=input("select option \n1.Employee\n2.owner")   
        if role==1:
            employee()
        else:
            owner()
display()
