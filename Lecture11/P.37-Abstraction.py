from abc import ABC, abstractclassmethod

class employee(ABC):
    def emp_id(self, id, name, age, salary): 
        pass

class childemployee1(employee):
    def emp_id(self, id):
        print("emp_id is 12345")

emp1 = childemployee1()
emp1.emp_id(id)