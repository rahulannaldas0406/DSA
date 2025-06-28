#Write a program to print the fibonacci number series up to a given number Expected output:0 1 1 2 3 5 8 13

'''a=0
b=1
n=5
while a<=n:
    print(a,end=" ")
    
    a,b=b,a+b'''

#using for loop 

'''a=0
b=1
for i in range(1,9):
    print(a,end=" ")
    a,b=b,a+b'''
#i learn a new type to swap a number in python 

'''a=2
b=3
print(a,b)
a,b=b,a
print(a,b)'''

#write a prime number
#Basic approach

'''num = int(input("Enter a number: "))
if num <= 1:
    print("Not Prime")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
    print(i)'''
#this is for in range 
'''9=starts
   51=end-1
    2=gap'''
'''for i in range(9,51,2):
    print(i)'''
#ARRAYS basic
array=[1,2,3,4]
print(array)


