class Employee:
    count = 0
    def __init__(self,name,salary):
        self.nme = name
        self.salary = salary
        Employee.count += 1

    def displaCount(self):
        print(Employee.count)

    def displayEmployee(self):
        print(self.nme,self.salary)

emp1 = Employee("张秋",2000)
emp1.age = 20
print(hasattr(emp1,'age'))
print(hasattr(emp1,'111'))