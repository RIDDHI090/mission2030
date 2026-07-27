print("===== Employee Information =====")

employee_name = input("Enter your name: ")
employee_ID = int(input("Enter your employee ID: "))
department = input("Enter your department: ")
salary = int(input("Enter your salary: "))
if salary >= 5000:
 print("seniour emplloy")
else:
 print("junior emplloy")

print("\n----- Employee Details -----")
print("Name      :", employee_name)
print("ID        :", employee_ID)
print("Department:", department)
print("Salary    :", salary)

