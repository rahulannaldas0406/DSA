'''Write a program to print sum 1 to 10 (initialize sum variable with 0)'''

'''sum=0
for i in range(0,10):
    sum=sum+i
print(sum)'''

#using while loop

'''sum=0
i=0
while(i<=10):
    sum=sum+i
    i=i+1
print(sum)'''

'''Write a program to print the nth power of a given number. n can be any positive number. (n=3 r =4 then answer must be 3*3*3*3 )'''
'''t=4
n=3
i=1
pow=1
while(i<=t):
   pow= pow*n
   i=i+1
print(pow)'''

n=int(input("enter a number:"))
t=int(input("enter power of the number:"))
pow=1
for i in range(0,t):
    pow=pow*n
print(pow)

