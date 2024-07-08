# #how to identify the given number is odd or even
# num1=input("Enter a number:")
# print(num1)

# if int(num1)%2 == 0:
#     if int(num1) <100:
#         print("Given number is less than 100")
#     print("This is even number")
# else:
#     print("This is odd number")
    
# #loop
# for i in range(1,1000):
#     if i==300:
#         print("I have got 300")
#         break
#     print(i)





# num = 5
# for i in range(1,num+1):
#     for j in range(i):
#         print("*", end="")
#     print()

# #list in python
# number_list = [3,4,5,6,7,25,26] #number in list

# #string in list
# fruit_list= ['Apple','banana','cheery','orange','grapes','watermelon']

# print(number_list[3])
# print(fruit_list)




# fruit_list= ['Apple','banana','cheery','orange','grapes','watermelon']
# print(fruit_list)



# for i in range(1,10):
#     new_fruits = input("Enter new fruits brought in department:")
#     if new_fruits=='exit':
#         break
#     fruit_list.append(new_fruits)
#     print("Fruits list after adding new item")
#     print(fruit_list)
    

    
    
    
#creating a empty list
fruits =[]

print("\t\t Welcome to fruits Department")

#creatng limit to manipulate data in the department
#The limit is user can only add or delete data from department 10 times
  
limit=10 
 
user_info = (
    'mode1':'2008'
    'colour':'black'
    
)
model = user_info.get('mode1')
print(user_info['mode1'])



while True:
    print("Add fruits name to append in the data list or remove from the data list")
    print("Press 1 to add item and 2 to delete item")   
    
    choose = input("choose the option: ")
    item = input("Enter fruits name: ")
    
    if int(choose) ==1:
        fruits.append(item)
        
    elif int(choose)==2:
        fruits.remove(item)
        print(fruits)
        
        