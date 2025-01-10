import csv

# Function to display the menu
def display_menu():
    print("Welcome to the Company HRM system!")
    print("1. Login")
    print("2. Exit")

# Function to authenticate user login
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if the username and password match
    if username == "kanchana" and password == "1234":
        print("Login successful!")
        while True:
            print("\n1. Add Employee")
            print("2. View Employees")
            print("3. Search Employee by ID")
            print("4. Calculate Employee Salary")
            print("5. Logout")
            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                add_employee()
            elif choice == '2':
                view_employees()
            elif choice == '3':
                search_employee()
            elif choice == '4':
                calculate_salary()
            elif choice == '5':
                print("Logging out...")
                break
            else:
                print("Invalid choice. Please try again.")
    else:
        print("Invalid username or password. Login failed.")

# Function to add an employee
def add_employee():
    emp_id = input("Enter employee ID: ")
    name = input("Enter employee name: ")
    age = input("Enter employee age: ")
    department = input("Enter employee department: ")

    with open('employees.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([emp_id, name, age, department])

    print("Employee added successfully!")

# Function to view all employees
def view_employees():
    with open('employees.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print("ID:", row[0])
            print("Name:", row[1])
            print("Age:", row[2])
            print("Department:", row[3])
            print("--------------------")

# Function to search employee by ID
def search_employee():
    emp_id = input("Enter employee ID: ")

    with open('employees.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == emp_id:
                print("Employee found!")
                print("ID:", row[0])
                print("Name:", row[1])
                print("Age:", row[2])
                print("Department:", row[3])
                return

    print("Employee not found!")

# Function to calculate employee salary
def calculate_salary():
    emp_id = input("Enter employee ID: ")
    working_hours = float(input("Enter working hours for the employee: "))
    cost_per_hour = float(input("Enter the cost per hour: "))

    salary = working_hours * cost_per_hour
    print("Employee ID:", emp_id)
    print("Working Hours:", working_hours)
    print("Salary:", salary)

# Main program loop
while True:
    display_menu()
    choice = input("Enter your choice (1-2): ")

    if choice == '1':
        login()
    elif choice == '2':
        print("Exiting the Company HRM system...")
        break
    else:
        print("Invalid choice. Please try again.")
