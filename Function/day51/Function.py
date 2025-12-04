#Find the power of any number using recursion.

'''def name(n):
    if n==0:
        return 
    print("Rahul")
    return name(n-1)
name(5)'''


'''def number(a,n):
    if n==0:
        return 
    print(a)
    return number(a+1,n-1)
number(1,5)'''

'''def num(n):
    if n==0:
        return 
    print(n)
    return num(n-1)
num(5)'''

#Find the sum of all even or odd numbers in a given range using recursion.

'''def ev_od(a,n):
    if a%2==0:
        print("Even:",a)
    else:
        print("odd:",a)
    if n==0:
        return
    return ev_od(a+1,n-1)
ev_od(1,20)'''

'''def even(a,n):
    if a>n:
        return 0
    if a%2==0:
        return a + even(a+1,n)
    else:
        return even(a+1,n)
print(even(1,10))'''

'''def odd(a,n):
    if a>n:
        return 0
    if a%2==0:
        return odd(a+1,n)
    else:
        return a+odd(a+1,n)
print(odd(1,10))'''


#Find reverse of any number using recursion.

'''def reverse(n):
    if n<=0:
        return ""
    a=n%10
    return str(a)+ "" + reverse(int(n//10))
print(reverse(12345))'''

'''def palindrome(n):
    rev=" "
    pal=n
    a=n%10
    rev+=str(a)
    print(rev)
    if n<=0:
        if rev==str(pal):
            return True
        else:
            return False
    
    return palindrome(n//10)
print(palindrome(12321))'''

def reverse_num(n, rev=""):
    if n == 0:
        return rev
    return reverse_num(n // 10, rev + str(n % 10))

def palindrome(n):
    rev = reverse_num(n)
    return rev == str(n)

print(palindrome(12321))
