# # # To define class we use class and its name

# # # class MyCollege:
# # #     pass
# # # print(type(MyCollege))

# # class MyCollege:
# #     x="Ram"
# # obj = MyCollege()
# # print(obj.x)



# # # This is how we create class with constructor
# # class ClassWithCons:
# #     def __init__(self) -> None:
# #         print("This is being called when initializing object")
# # obj1=ClassWithCons()



# # # This is how we pass parameter(data) to class
# # class ClassWithData:
# #     def __init__(self,name,address) -> None:
# #         self.name=name
# #         self.address=address

# #         print(name)
# #         print(address)
# # obj2=ClassWithData("Raj","Bramakhel")


# # # This is how we add multiple function in a class
# # class MultipleFunctionClass:
# #     def __init__(self,name,age,address) -> None:# we need to always _init_ in class 
# #         self.name=name#these are variables
# #         self.age=age#same as abv
# #         self.address=address#same as abv
# #     def printName(self):
# #         print(self.name)

# #     def printAge(self):
# #         print(self.age)

# #     def printAddress(self):
# #         print(self.address)

# # obj3=MultipleFunctionClass("Rudra","20","Chabahil")
# # obj3.printName()
# # obj3.printAge
# # obj3.printAddress()




# # Inheritance in class
# class ParentClass:
#     def __init__(self,name) -> None:
#         self.name=name
#         self.class_type="BSCIT"
#         print("This is parent class")

#     def printName(self):
#         print(self.name)

# # Here we are inheriting the parent class
# class ChildClass(ParentClass):
#     def __init__(self, name) -> None:
#         super().__init__(name)

# obj1=ChildClass("Raj")
# print(obj1.class_type)
# obj1.printName()

#Class Parent2
class Parent2:
    def __init__(self,name,address) -> None:
        self.name=name
        self.address=address

        print("This is being called from parent class")
        print(f"{self.name}{self.address}")
class Child2(Parent2):
    def printNumber(Self):
        print("This is number")

obj3=Child2("Raj","Bramakhel")
obj4=Child2("Bibek","Boudha")
boj5=Child2("Ramesh","Sindhuli")
# obj3.printNumber()