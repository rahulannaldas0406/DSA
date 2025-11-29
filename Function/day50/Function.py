#Cube of any number using the function.


'''def cube(n):
    cub=1
    for i in range(0,3):
        cub*=n
    return cub
print(cube(2))'''

'''def cube(n):
    return n**3
print(cube(3))'''

#Find diameter, circumference and area of a circle using functions.

'''import math

def circle_properties(r):
    d = 2 * r
    c = 2 * math.pi * r
    a = math.pi * r ** 2
    return d, c, a

diam, circ, ar = circle_properties(5)
print("Diameter:", diam)
print("Circumference:", circ)
print("Area:", ar)'''


'''def circle(r):
    d=2*r
    c=2*3.14*r
    a=3.14*r**2
    return a,c,a
diam,circ,ar=circle(5)
print("Diameter:",diam)
print("circumstance:",circ)
print("Area:",ar)'''

'''def diameter(r):
    return 2 * r

def circumference(r):
    return 2 * 3.14 * r

def area(r):
    return 3.14 * r * r

# Example
r = 5
print("Diameter:", diameter(r))
print("Circumference:", circumference(r))
print("Area:", area(r))'''


#Maximum and minimum between two numbers using functions.

'''def max_min(a,b):
    if a>b:
        return str(a)+"is maximum",str(b)+"is minimum"
    if a<b:
        return str(b)+"is maximum",str(a)+"is minimum"


print(max_min(5,4))'''

'''def max_num(a, b):
    if a > b:
        return a
    else:
        return b

def min_num(a, b):
    if a < b:
        return a
    else:
        return b

mx = max_num(4, 5)
mn = min_num(4, 5)

print("max is", mx)
print("min is", mn)'''

#Check whether a number is even or odd using functions

'''def ev_od(n):
    if n%2==0:
        return "It is Even"
    else:
        return "It is odd"
print(ev_od(4))'''

'''def is_even(n):
    if n == 0:
        return True
    elif n == 1:
        return False
    else:
        return is_even(n - 2)

def is_odd(n):
    return not is_even(n)

# Example
num = 7
if is_even(num):
    print("Even")
else:
    print("Odd")
'''

#Check whether a number is prime, Armstrong or perfect number using functions

'''def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def ams(n):
    nm=n
    value=0
    num=str(n)
    pow=len(num)
    while nm>0:
        res=nm%10
        value+=res**pow
        nm=nm//10
    if value == n:
        return True
    else:
        return False

def is_perfect(n):
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    return s == n
        

n=77
if is_prime(n):
    print("It is prime")
elif ams(n):
    print("Amstrong")
elif is_perfect(n):
    print("Perfect number")
else:
    print("It is neither prime, Armstrong nor perfect")'''

#Find all prime numbers between the given interval using functions.

'''def prime_num(a, b):
    arr = []
    for i in range(a, b + 1):
        if i < 2:
            continue
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                break
        else:
            arr = arr + [i]    # Add element without append
    return arr

print(prime_num(2, 9))'''

#Print all strong numbers between the given interval using functions.


'''def strong_num(a, b):
    
    for n in range(a,b+1):
        num=n
        sum=0
        while num>0:
            mul=1
            temp=num%10
            for i in range(temp,0,-1):
                mul*=i
            sum+=mul
            num=num//10
        if n==sum:
            print(sum)


strong_num(1, 145)'''

# n=3

# sum=0
# while n>0:
#     mul=1
#     temp=n%10
#     for i in range(temp,0,-1):
#         mul*=i
#     sum+=mul
#     n=n//10
# print(sum)

#Armstrong numbers between the given interval using functions.

'''def amstrong_num(a, b):
    
    for n in range(a,b+1):
        nm=n
        value=0
        num=str(n)
        pow=len(num)
        while nm>0:
            res=nm%10
            value+=res**pow
            nm=nm//10
        if value == n:
           print(n)
       


amstrong_num(153, 10000)'''


#Print all perfect numbers between the given interval using functions.

'''def perfect_num(a, b):
    
    for n in range(a,b+1):
        s = 0
        for i in range(1, n):
            if n % i == 0:
                s += i
        if s==n:
            print(s)
    
       
perfect_num(1, 100)'''