# Level 3 Question 15

a = [12 , 45, 3 , 98 , 7 , 34 , 21]
# a ) print the numbers :
for i in a :
    print(i)

# b ) print only numbers greater than 30 
count = 0
for j in a :
    if(j > 30):
        print(j)
        count += 1

# c ) count how many numbers are greater than 30
count = 0 
for k in a :
    if(k>30 ):
        count += 1
print(count)
