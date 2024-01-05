#libary management system
import time

print("\n\n\t\twelcome to abc libary \n\t\t\tNaikap,ktm")

def books():
    book1 = {
    'name': 'Introduction to Python',
    'price': 29.99,
    'author': 'John Doe',
    'edition': '1st Edition'
        }

    book2 = {
    'name': 'Data Science Essentials',
    'price': 39.99,
    'author': 'Jane Smith',
    'edition': '2nd Edition'
        }

    book3 = {
    'name': 'The Art of Programming',
    'price': 49.99,
    'author': 'Sam Johnson',
    'edition': '3rd Edition'
        }
    book_name = input("Enter the name of the book you want to borrow : \t>")
    print('\n\t\tSearching...')
    if book_name == "1":
        return book1
    elif book_name == "2":
        return book2
    else:
        return book3
    #needed to modify
def new_mem():
    error = False
    while error !=True:  
        try:
            detail = {
                    "Name": input("Enter name :"),
                    "Contact": input("Enter contact no.:"),
                    "Address": input("Enter address :"),
                    "Email": input("Enter email id :")
                    }
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
    mem_name = input("Enter your name: ")
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

        with open("employeee.txt", "r") as file:
            lines = file.readlines()
        
        for line in lines:
            if emp_name in line:
                found = True
                print("Record Found!")
                print("---------------------------")
                print(line)
                break

        if not found:
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
    edit=input("Select option\n1. Add employee data\n2. View emplyee record\n3. Edit employee details")
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
    else:
         print("wait")        
def owner():
    own_password=input("Enter a password: ")  
    # if own_password=='my_shop':
    if own_password=='1':
        monitor=input("Select option:\n1>Data of employee\n2>Data of visitor\n>") 
        if monitor==2:
            visitor_details()
        else:
            employee_details()

def display():
    position=int(input("\tSelect option:\n1.New visitor\n2.Old visitor\n3.other\n>>"))

    if position==1:
        new_mem()
        books()
        
                
    elif position==2:
        old_mem()
        

    elif position == 3:
        print("Other option selected. Implement the logic for 'Other' here.")
        employee()

# display()
#118
details={"Name":input("Enter name :"),
                 "Education":input("Enter your education :"),
                 "Experiences":input("Enter your experiences :"),
                 "issued_date":time.asctime(time.localtime(time.time()))}
with open("employeee.txt",'a+') as f:
            f.write("\n"+str(details))