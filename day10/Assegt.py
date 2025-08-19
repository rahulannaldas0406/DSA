#using function write below problems
'''1 factorial
   2 prime number
   3 fibonicc series
   4 count digits
   '''              
#factorial

'''def factorial(num):
    fac=1
    while num>0:
        fac=fac*num
        num=num-1
    print(fac)
factorial(5)'''

#check prime number
'''def Prime(num):
    if num<2:
        return True
    for i in range(2,num):
        if num%i==0:
            return False
        else:
            return True
print(Prime(3))'''

#fibinoicc series
'''def fib(num):
    a,b=0,1
    for i in range(0,num):
        print(a,end=" ")
        a,b=b,a+b
fib(5)'''
#reverse a number
a=[1,2,3]
space=""
for i in range(len(a)):
    space=str(a[i])+space

print(space)
a[3]
for j in range(len(space)):
    a[j]=a[j]+space[j]
print(a[j])

'''a=[1,2,3,4,5]
print(len(a))'''
'''class Solution(object):
    def fib(self, n):
        if n==0|n==1:
            return n
        
        for i in range(2,n):
            self=a+b
            a,b=b,a+b
        return self'''