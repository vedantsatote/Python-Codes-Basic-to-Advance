class Employee:
    def __init__(self, name, position, salary_per_month):
        self.name = name
        self.position = position
        self.salary_per_month = salary_per_month
    
    def annual_salary(self):
        return self.salary_per_month * 12

# Creating instances of Employee
employee1 = Employee("John", "Software Engineer", 5000)
employee2 = Employee("Emma", "Data Analyst", 4500)

# Calculating and displaying annual salaries
print(f"{employee1.name}'s annual salary: ${employee1.annual_salary()}")
print(f"{employee2.name}'s annual salary: ${employee2.annual_salary()}")
