'''def hello():
    return 'Hello World'
print(hello())'''

#Greatest number using function

'''def Gnum(a,b):
    if a>b:
        return a
    else:
        return b
x,y=map(int,input("enter a two number:").split())
value=Gnum(x,y)
print(value)'''

#mark on mpc course  


'''def marks(m,p,c):
    avg=int(m)+int(p)+int(c)
    if(avg==300):
        print("Grade O")
    elif(avg>=250 & avg<300):
        print("Grade A+")
    elif(avg>=200 & avg<250):
        print("Grade A")
    elif(avg>=150&avg<200):
        print("Grade B+")
    elif(avg>=100&avg<150):
        print("Grade B")
    elif(avg>=50&avg<100):
        print("Grade C")
    elif(avg>=0&avg<50):
        print("Fail")
maths,scie,chem=map(int,input("enter Three subjects marks:").split())
value=marks(maths,scie,chem)
print(value)'''

#Write a function that takes an integer and returns the number of digits in it.

'''def count_digits(num):
    count=0
    for i in str(num):
        count+=1
    return count
print(count_digits(1234))'''

#Given a list, return the sum of squares of all even numbers

'''def Sum_evensqrs(num):
    li=[]
    sum=0
    for i in num:
        if i%2==0:
            sum+=i**2
    li.append(sum)
    return li
        
print(Sum_evensqrs([1,2,3,4]))'''

#Write a function that mimics Python’s built-in range(start, stop, step) using a while loop.

'''def custom_range(start,stop,step):
    li=[]
    for i in range(start,stop,step):
        li.append(i)
    return li
print(custom_range(2,10,2))'''

#Write a function to return the greatest common divisor (GCD) of two numbers.

'''def GCD(a,b):
    while b!=0:
        a,b=b,a%b
    return a
print(GCD(30,60))'''






