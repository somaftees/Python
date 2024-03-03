number = [1,2,3,4,5,6,7,8,9]
x=0
z=0
for i in number:
    if i % 2 == 0:
        x+=1
    else:
        z+=1
        
print("The Number of even numbers = ",x)
print("The Number of odd numbers = ",z)
