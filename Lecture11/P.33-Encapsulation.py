class employee(object):
    def __init__(self) -> None:
        self.name = "peter"
        self._age = 45
        self.__salary = 35000

object1 = employee()
print(object1.name)
print(object1._age)
print(object1.__salary)
