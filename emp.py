import json

class Employee:
    def __init__(self, name, employee_id, title, department):
        self.name = name
        self.employee_id = employee_id
        self.title = title
        self.department = department

    def display_details(self):
        print(f"Name: {self.name}, ID: {self.employee_id}, Title: {self.title}, Department: {self.department}")

    def __str__(self):
        return f"{self.name} - ID: {self.employee_id}"

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, employee):
        self.employees.remove(employee)

    def list_employees(self):
        for employee in self.employees:
            print(employee)

class Company:
    def __init__(self):
        self.departments = {}

    def add_department(self, department):
        self.departments[department.name] = department

    def remove_department(self, department_name):
        del self.departments[department_name]

    def display_departments(self):
        for department_name, department in self.departments.items():
            print(f"Department: {department_name}")
            department.list_employees()

def print_menu():
    print("\nEmployee Management System Menu:")
    print("1. Add Employee")
    print("2. Remove Employee")
    print("3. Add Department")
    print("4. Remove Department")
    print("5. Display Departments")
    print("6. Exit")

def save_data(company):
    with open('company_data.json', 'w') as file:
        data = {department_name: [str(employee) for employee in department.employees]
                for department_name, department in company.departments.items()}
        json.dump(data, file)

def load_data():
    try:
        with open('company_data.json', 'r') as file:
            data = json.load(file)
            company = Company()
            for department_name, employees in data.items():
                department = Department(department_name)
                for employee_str in employees:
                    name, emp_id = employee_str.split(' - ID: ')
                    employee = Employee(name, int(emp_id), "", department_name)
                    department.add_employee(employee)
                company.add_department(department)
            return company
    except FileNotFoundError:
        return Company()

def main():
    company = load_data()

    while True:
        print_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter employee name: ")
            emp_id = int(input("Enter employee ID: "))
            title = input("Enter employee title: ")
            department_name = input("Enter department name: ")

            employee = Employee(name, emp_id, title, department_name)
            if department_name in company.departments:
                company.departments[department_name].add_employee(employee)
            else:
                print(f"Department '{department_name}' does not exist. Please add the department first.")

        elif choice == '2':
            department_name = input("Enter department name: ")
            if department_name in company.departments:
                company.departments[department_name].list_employees()
                emp_id = int(input("Enter employee ID to remove: "))
                for employee in company.departments[department_name].employees:
                    if employee.employee_id == emp_id:
                        company.departments[department_name].remove_employee(employee)
                        print(f"Employee {employee.name} removed from department {department_name}.")
                        break
                else:
                    print(f"Employee with ID {emp_id} not found in department {department_name}.")
            else:
                print(f"Department '{department_name}' does not exist.")

        elif choice == '3':
            department_name = input("Enter department name: ")
            department = Department(department_name)
            company.add_department(department)
            print(f"Department '{department_name}' added.")

        elif choice == '4':
            department_name = input("Enter department name to remove: ")
            if department_name in company.departments:
                company.remove_department(department_name)
                print(f"Department '{department_name}' removed.")
            else:
                print(f"Department '{department_name}' does not exist.")

        elif choice == '5':
            company.display_departments()

        elif choice == '6':
            save_data(company)
            print("Exiting the Employee Management System. Data saved.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
