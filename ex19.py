# Level Question 19

grades = [85, 92, 78, 65, 88, 91, 73, 89, 55, 94]

A = 0
B = 0
C = 0
below_70 = 0 

for a in grades :
    if(a>=90):
        A += 1
        
    elif(a>= 80 ):
        B += 1
        
    elif(a >= 70 ) :
        C += 1
        
    else:
        below_70 += 1
        
print("The number of students who got A is : " , A)
print("The number of students who got B is : " ,B)
print("The number of students who got C is : " , C)
print("The number of students who got below 70 is : " ,below_70)