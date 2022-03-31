# private field
# class Geek:
#     __name = None
#     __roll = None
#     __branch = None
#     def __init__(self, name, roll, branch):
#         self.__name = name
#         self.__roll = roll
#         self.__branch = branch
#     def __displayDetails(self):
#                print("Name: ", self.__name)
#                print("Roll: ", self.__roll)
#                print("Branch: ", self.__branch)
#     def accessPrivateFunction(self) :
#               self.__displayDetails()
# obj = Geek("R2J", 1706256, "information technology")
# obj.accessPrivateFunction()


# public field
# class Geek:
#     def __init__(self, name, age):
#         self.geekName = name
#         self.geekAge = age
#     def displayAge(self):
#         print("Age: ", self.geekAge)
# obj = Geek("R2J", 20)
# print("Name: ", obj.geekName)
# obj.displayAge()


#  protected field
class Student:
    _name = None
    _roll = None
    _branch = None
    def __init__(self, name, roll, branch):
        self._name = name
        self._roll = roll
        self._branch = branch
    def _displayRollAndBranch(self):
        print("Roll: ", self._roll)
        print("Branch: ", self._branch)
class Geek(Student):
    def __init__(self, name, roll, branch ):
        Student.__init__(self, name, roll, branch)
    def displayDetails(self):
        print("Name: ", self._name)
        self._displayRollAndBranch()
obj = Geek("R2J", 1706256, "information technology")
obj.displayDetails()

