from datetime import date

class Employee:

    def __init__ (self, employee_name , employee_age, employee_salary, employment_year):
       self.name = employee_name
       self.age = employee_age
       self.salary = employee_salary
       self.employment_year = employment_year

    def get_working_years(self):
        current_year = date.today().year
        return current_year - self.employment_year

    def __str__(self):
        return 'Employee (name= '+ self.name +', age= '+ str(self.age) +', salary= '+ str(self.salary) +', employment year: '+ str(self.employment_year) + ')'

class Manager(Employee):

    def __init__(self, employee_name , employee_age, employee_salary, employment_year, bonus):
        super().__init__(employee_name , employee_age, employee_salary, employment_year)
        self.bonus_percentage = bonus

    def get_working_years(self):
        current_year = date.today().year
        return current_year - self.employment_year

    def get_bonus(self):
        return self.bonus_percentage * self.salary

    def __str__(self):
        return 'Manager (name= '+ self.name +', age= '+ str(self.age) +', salary= '+ str(self.salary) +', employment year: '+ str(self.employment_year) + ', bonus: '+str(self.bonus_percentage) + ')'


def main():
    employees = []
    managers = []

    print ("Options:")
    print ("    1. Show Employees")
    print ("    2. Show Managers")
    print ("    3. Add An Employee")
    print ("    4. Add A Manager")
    print ("    5. Exit")

    x = int(input ("Please choose an option from 1-5: "))


    while x != 5 :
        if x == 1:
            print("***************************")
            print("Employees: ")
            for item in employees:
                print(item)
        elif x == 2:
            print("***************************")
            print("Managers: ")
            for item in managers:
                print(item)
        elif x == 3:
            print("***************************")
            print ("Enter employee info: ")
            name = input("name: ")
            age = input("age: ")
            salary = float(input("salary: "))
            year = int(input("employment date: "))
            newemp = Employee(name,age,salary,year)
            employees.append(newemp)
        elif x == 4:
            print("***************************")
            print("Enter manager info: ")
            name = input("name: ")
            age = input("age: ")
            salary = float(input("salary: "))
            year = int(input("employment date: "))
            bonus = float(input("bonus salary: "))
            newman = Manager(name,age,salary,year,bonus)
            managers.append(newman)
        print ("Options:")
        print ("    1. Show Employees")
        print ("    2. Show Managers")
        print ("    3. Add An Employee")
        print ("    4. Add A Manager")
        print ("    5. Exit")

        x = int(input ("Please choose an option from 1-5: "))



if __name__ == '__main__':
	main()
