def employee_detail(name,department,salary):
    print("============================")
    
    print("Hello", name)
    print("Department", department)
    print("Salary", salary)
    print("Welcome to 2030 company")

    print("============================")

employee = input("Enter employee name: ")
department = input("Enter your department: ")
salary = int(input("Enter your salary: "))

employee_detail(employee,department,salary)
employee_detail("Pal","IT",20000)
