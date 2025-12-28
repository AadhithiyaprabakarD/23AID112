# Level 3 Question 17
a = [23 , 1 , 45 , 98, 67, 31, 59, 89, 35]

biggest = a[0]
smallest = a[0]
for i in a:
    if(i > biggest):
      biggest = i
    if(i< smallest):
      smallest = i
print("The biggest number is : ", biggest)
print("The smallest number is : ", smallest)