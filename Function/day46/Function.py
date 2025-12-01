#Write a function which can return the factorial of a number.
                            
'''def fac(n):

    result=1
    for i in range(1,n+1):
        result*=i
    print(result)
fac(4)'''

#Write a function which can to return the reverse of a given number.


'''def rev(n):
    num=str(n)
    result=" "
    for i in range(len(num)-1,-1,-1):
        result+=num[i]
    return int(result)
print(rev(1234))'''

#Write a function which can check a given number is prime number or not

'''def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(is_prime(5))'''

#Write a function which can check a given number is palindrome or not

'''def palid(n): 
    num=str(n) 
    result="" 
    for i in range(len(num)-1,-1,-1): 
        result+=num[i] 
    if n==int(result): 
            return True 
    else: return False 
print(palid(543456))'''