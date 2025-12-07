#Write a function which can to display the reverse of a given number

'''def rev(n):
    
    res=""
    while n>0:
        temp=n%10
        res=res+str(temp)
        n=n//10
    return res
print(rev(1234))'''

'''def rev(n):
    return str(n)[::-1]

print(rev(1234))'''

#Write a function which can check a given number is armstrong number or not

'''def ams(n):
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
        
    

print(ams(153))'''

#Write a function which can return the factorial of a number to another variable


'''def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

result = factorial(5)
print(result)'''

#Write a function to display the number of digits in the given number

'''def num_dig(n):
    count=0
    for i in range(0,len(str(n))):
        count+=1
    return count
print(num_dig(123455))'''

#Write a function that returns an array of all even numbers between 1 and 20.


'''def even(arr):
    arr1=[0]*len(arr)
    j=0
    for i in range(0,len(arr)):
        if arr[i]%2==0:
            arr1[j]=arr[i]
            j+=1
    return arr1[0:10]
            
        
print(even([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]))'''







