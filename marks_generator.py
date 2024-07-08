print("This is mark generator")

# showing user other information about marks
#generator

#To show anything in written form we use print()

print("\t\t\t Marks generator created by Rijan")

#To create it we need to take user marks in each subject

Social= input("Enter a marks in Social: ")

Science= input("Enter a marks in Science: ")

Nepali= input("Enter a marks in Nepali: ")

Math= input("Enter a marks in Math: ")

gk= input("Enter a marks in gk: ")


print("Your marks in total")

#Getting total marks by adding marks of each subjects

total_marks= int(Science) + int(Social) + int(Nepali) + int(Math) + int(gk)

#without Using concatinate
print("Your total marks is :",total_marks)

#using concatinate
# print("Your total marks is: " +str(total_marks))

#To get percentage of a student we calculate like this
#Total contained Marks divided by Total marks of all subject multiply by 100

total_percentage = total_marks/5

print("Your total percentage is: ", total_percentage)

#using if else condition to show division or distinction

if total_percentage>=80 and total_percentage<=100:
    print("You have got 1st division")

elif total_percentage>=60 and total_percentage<=79:
    print("You have got 2nd division")
    
elif total_percentage>=40 and total_percentage<=59:
    print("You have got 3rd division")
    
else:
    print("You are fail")
    

