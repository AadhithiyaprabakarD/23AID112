# Level 2 Question 6

age = int(input("Enter your age : "))

if(age < 13):
    print("You are a child")
elif(age>=13 and age<=17):
    print("You are a teenager")
elif(age>=18 and age<=64):
    print("You are an adult")
else:
    print("You are a senior")