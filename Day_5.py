# ####String_operation###


# strng_name = "This is a string"
# print(strng_name)
# print(len(strng_name))


# # car_list = [
# #     'ford', 'maruti','suzuki',
# # ]
# # print(car_list)


# a ='hello world'
# print(a[6])

# for i in a:
#     print(i)
    
# email = input("Enter your email:")

# # checking if the value present in string
# if '@' not in email:
#     print("Email is not valid")
# else:
#     print("Email validated successfull")
    
# example = "Favourite food is apple"

# # #checking if a value present in string
# # if 'apple' in example:
# #     print("Yes apple is fav")
    
# # #slicing in string

# print(example[2:8])
 
#  # slicing getting from last indexing
# print(example[-1])

# # slicing without denoting begining index
# print(example[:10])

# # This slicing will give all value from given begining indexing to last
# print(example[10:])

# b= "hello world!"
# print(b[-5:-2])

# #modifying string
# sentence="The world is beautiful"

# # To make all element inside string into lowercase
# print(sentence.lower())

# # to make all element inside string into uppercase
# upper_sentence= sentence.upper()

# print(sentence.upper())

# # Removing whitespace from the string
# # whitespace means unwanted space in the sentence

new_sentence = " texas college of mangement and IT"
print(new_sentence.strip())

# To replace anything character and a word from a string we use replace
new_sentence.strip().replace('college','school')
print(new_sentence)
print(len(new_sentence))


# splitting the string
split_name = "Rajesh!hamal"
print(split_name.split('!'))
print(type(split_name.split('!')))

#string concatination (Joining the string)
first_name ='Rijan'
last_name ='singh'

concate_name = first_name+"   "+last_name
print(concate_name)
print(first_name+"   "+last_name)





def sum(a,b) :
    su = a+b
    return su

sum_amt = sum(10,20)
print(sum_amt)


# there is two way of formatting string and variable
print("The sum of 10 and 20 is", sum_amt,"The subtract of 50 and 20 is ", sum_amt)
print("The sum of 10 and 20 is " + str(sum_amt))

print(f"The sum of 10 and 20{sum_amt}")


print(f"{sum_amt} is the total sum")

#we can perform any arthmetic operation within {} while formating string
print(f"{4*8} is multiply value of 4 and 8")

print("Basanti prasad koirala wrote \"mia khalifa\" ")


name = "sao is the great man"










