import datetime

class Employee:

    def __init__ (self, employee_name , employee_age, employee_salary, employment_year):
       self.name = employee_name
       self.age = employee_age
       self.salary = employee_salary
       self.year = employment_year

    def get_working_years(self):
        today = datetime.datetime.now()
        return int(today - self.year)

    def __str__(self):
        return 'Employee (name= '+ self.name +', age= '+ str(self.age) +', salary= '+ self.salary +', employment year: '+ self.year + ')'

class Manager(Employee):

    def __init__(self, employee_name , employee_age, employee_salary, employment_year, bonus_percentage):
        super().__init__(employee_name , employee_age, employee_salary, employment_year)
        self.bonus = bonus_percentage

    def get_working_years(self):
        today = datetime.datetime.now()
        return int(today - self.year)

    def get_bonus(self):
        return self.bonus * self.salary

    def __str__(self):
        return 'Manager (name= '+ self.name +', age= '+ str(self.age) +', salary= '+ self.salary +', employment year: '+ self.year + ', bonus: '+self.bonus+ ')'


def main():
    employees = []
    managers = []

    x = input ("Please choose an option from 1-5: ")
    print ("Options:")
    print ("    1. Show Employees")
    print ("    2. Show Managers")
    print ("    3. Add An Employee")
    print ("    4. Add A Manager")
    print ("    5. Exit")

    while 0 < x < 6 :
        if x == 1:
            print (employees)
        elif x == 2:
            print (managers)
        elif x == 3:
            print ("Enter employee info: ")
            newemp = Employee()
            newemp.name = input("name: ")
            newemp.age = input("age: ")
            newemp.salary = input("salary: ")
            newemp.year = input("employment date: ")
        elif x == 4:
            print("Enter manager info: ")
            newman = Manager()
            newman.name = input("name: ")
            newman.age = input("age: ")
            newman.salary = input("salary: ")
            newman.year = input("employment date: ")
            newman.bonus = input("manager's bonus: ")
        elif x == 5:
            break
        else:
            print("invalid input")



if __name__ == '__main__':
	main()
