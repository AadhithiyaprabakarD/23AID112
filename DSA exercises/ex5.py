# Level 1 Question 5

num1 = input("Enter your first number : ")
num2 = input("Enter your second number : ")

number1 = int(num1)
number2 = int(num2)

sum = number1+number2
difference = number1 - number2
product = number1*number2

print("The sum of the numbers is " , sum)
print("The difference of the numbers is ", difference)
print("The product of the numbers is ", product)

if(number1>number2):
    print(number1 ," is greater than " , number2 )
elif(number1==number2):
    print("Both the numbers are equal")
else:
    print(number2 , " is greater than " ,number1)

