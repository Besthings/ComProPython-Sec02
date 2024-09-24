from abc import ABC, abstractmethod

class AbcClass(ABC):
    def print(self, x):
        print("Passed value: ", x)

    @abstractmethod
    def task(self):
        print("We are inside AbcClass task")

class test_class(AbcClass):
    def task(self):
        print("We are inside test_class task")

class example_class(AbcClass):
    def task(self):
        print("We are inside example_class task")

# object of test_class created
test_obj = test_class()
test_obj.task()
test_obj.print(100)

# object of example_class created
example_obj = example_class()
example_obj.task()
example_obj.print(200)

print("test_obj is instance of AbcClass?", isinstance(test_obj, AbcClass))
print("example_obj is instance of AbcClass?", isinstance(example_obj, AbcClass))