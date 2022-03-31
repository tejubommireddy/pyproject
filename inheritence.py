# A is a super class. B is a sub class of A. C is a sub class of B
# class A:
#     pass
# class B(A):
#     pass
# class C(B):
#     pass
# x = C()
# print(isinstance(x, A))

# method overriding
# class parent:
#     def anything(self):
#         print('function defined in parent class!')
# class child(parent):
#     pass
# obj2 = child()
# obj2.anything()

# over riden method in classes objects
# class Animal:
#     def walk(self):
#         print('hello, i am the parent class')
# class Dog(Animal):
#     def walk(self):
#         print('hello. i am the child class')
# print('the method walk here is ovrriden in the code')
# r = Dog()
# r.walk()
# r = Animal()
# r.walk()

# runtime poly morphism
# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def info(self):
#         print(f"i am a cat.my name is {self.name}.i am{self.age} years old.")
#     def make_sound(self):
#         print("meow")
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def info(self):
#         print(f"i am a dog.my name is {self.name}. i am {self.age} years old.")
#     def make_sound(self):
#             print("bark")
# cat1 = Cat("kitty", 2.5)
# dog1 = Dog("fluffy", 4)
# for animal in (cat1, dog1):
#         animal.make_sound()
#         animal.info()
#         animal.make_sound()
