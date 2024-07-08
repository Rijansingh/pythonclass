# # There are two types of function i.e Inbuilt function and user defined function
# # Example of inbuilt function are: print(), len() ,count(), input(), lower()


# #Example of user defined function
# def myfunction(): #here myfunction is a name of function
#     print("This is function")
    
# myfunction()


# #How to perform calculation within function
# # Example of function calculation something with any parameter
# def calculate():
#     num1 = 34
#     num2 =54
    
#     multiply = num1 * num2
    
#     print(multiply)
    
# #To call the above calculation we call the function
# calculate()

# #How to return any operation from function
# def returningFunction():
#     num1 = 30
#     num2 = 200
    
#     return num1+num2

# return_data = returningFunction()
# print(return_data)

# #How to send parameter as an argument of function and perform operation

# def parameterFunction(num1,num2,num3,Name):
#     print(num1)
#     print(num2)
#     print(num3)
    
# # Sending parameter to function
# num1 = input("Enter number 1: ")
# parameterFunction(20,30,40,'Ram')


# # How to perform operation inside function using parameters
# def paraFunction(name,year):
#     pass
#     print("The user name is: ", naming)
#     current_year = 2024
#     real_age = current_year - int(year)
    
#     return real_age


# name = input("Enter your name: ")
# year = input("Enter your year: ")


# real_birth_year = paraFunction(name,age)

# print("Your birth year is: ",real_birth_year)

# How to handle arbitary arguments
def arbiFunction(*args):
    
    print(args)
    selected_user = ['Ram','Ajay']
    print(args)
    for i in selected_user:
        print("Selected user argument found",i)
    
arbiFunction("Ram","shishir","Raj","Rijan","Manoj","Ajay","Samar","sundar")



# How to handle keyword agruments
def kwFunction(**kwargs):
    #It is in dictionary form
    print(kwargs)

kwFunction(name1 = "Ram", name2= "Sam", name3= "Ramesh")


#Default value function
def defaultValueFunction(country = "Nepal",city="kathmandu"):
    print("Your country is ",country)
    print("Your city is ",city)
    
defaultValueFunction(country= "Japan")



# How to define and access global variable
street = "Jorpati"
def globalChangeFunction():
    global street
    street = "Chabel"
    print(street)
    
globalChangeFunction()

print(street)

    

