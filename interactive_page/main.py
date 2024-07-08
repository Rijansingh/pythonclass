import calculate
import oddeven



print("\t welcome here please select your option:")
print("\t choose 1 for odd even and 2 for calculation")

choose_opt = input("Enter your option: ")

if choose_opt == "1":
    num = input("enter number to find odd even:")
    old_even_result = oddeven.findOddEven(num)
    if old_even_result:
        print("This number is even")
    else:
        print("This is odd number")
        
elif choose_opt == "2":
    num1= input("Enter number 1: ")
    num2= input("Enter number 2: ")
    sum_data = calculate.calc(int(num1), int(num2))
    print("The sum is ", sum_data)
else:
    print("Option is not available")    



