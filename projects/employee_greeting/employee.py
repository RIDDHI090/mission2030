def employee_detail(name,department,salary,city):
    print("============================")
    
    print("Hello", name)
    print("Department", department)
    print("Salary", salary)
    print("City", city)
    print("Welcome to 2030 company")
    
    print("============================")

employee = input("Enter employee name: ")
department = input("Enter your department: ")
salary = int(input("Enter your salary: "))
city = input("Enter city: ")

employee_detail(employee,department,salary,city)
employee_detail("Pal","IT",20000,"surat")
