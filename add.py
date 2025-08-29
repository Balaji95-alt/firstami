# add to two numbers......

# num1= 30
# num2 = 40
# sum =num1+num2
# print("The sum of the number is ",sum)


#############user get input#########################
# num1 =int(input("Enter the value1:"))
# num2=int(input("Enter the value2:"))
# num1 =float(input("Enter the value1:"))
# num2=float(input("Enter the value2:"))
# sum = num1+num2
# print("The sum of the number is", sum)


#################### odd or even number@########################

# num=int(input("Enter the value1:"))

# if num % 2==0:
#     print ("this is even number")
# else:
#     print ("this is odd number")
    
############### positive negative number find################
   
# num=int(input("Enter the number:"))

# if num > 0 :
#    print("Positive number")
   
# elif num ==0:
#    print("ZERO")    
# else:
#     print ("negative")      

################### How to find prime number #####################

# num=int(input("Enter the  value:"))
# flag=False
# # 
# if num >1:
#    for i in range(2, num // 2):
#        if num % i ==0:
#         flag = True
#         break   
# if flag: 
#     print(num,"is not a prime number")
# else:
#     print(num, "is a prime number")
                
#palindrome

# num=int(input("Enter the value:"))
# rev = 0
# temp = num

# while num > 0:
#     reminder= num %  10
#     rev=(rev *10 )+ reminder
#     num = num //10
# if temp == rev:
#     print(temp,"is a pallinderme")    
# else: 
#     print(temp,"non")   


#***************interchange Bill***************

# n1= int(input("Enter the value1:"))
# n2= int(input("Enter the value2:"))

# print("Value of number1:",n1)
# print("value of number2:",n2)
# print("***************************************")

# temp=n1
# n1=n2
# n2=temp
# print("Value of number1:",n1)
# print("value of number2:",n2)

# factorial number##############################
# num=int(input("Enter the value1:"))
# factorial = 1

# if num < 0:
#     print ("factorial not negative value")
# elif num == 0:
#     print("factorial is not zero")
# else:
#     for i in  range(1, num+1):
#         factorial = factorial * i 
#     print("Factorial is ",factorial)           
#find the maximum number

num1=int(input("Enter the value1:"))
num2=int(input("Enter the value2:"))

if num1 > num2:
    print("num1 is maximum")
    
elif num1 < num2:
    print ("number 2 maxmium")   
else:
    print(" minimum")    
           