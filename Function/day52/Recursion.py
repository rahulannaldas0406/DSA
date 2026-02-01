#Find the sum of digits of a given number using recursion.

'''def sum_digit(n):
    if n<=0:
        return 0
    a=n%10
    return a + sum_digit(n//10)
print(sum_digit(12345))'''

#there are four more approach is there so you can check in chatGPT

#Find factorial of any number using recursion.

'''def fac(n):
    if n==0:
        return 1
    return n*fac(n-1) 
print(fac(5))'''

'''def factorial(n):
    def helper(n, ans):
        if n == 0:
            return ans
        return helper(n - 1, ans * n)
    return helper(n, 1)'''

'''def factorial(n):
    
    return helper(n, 1)

def helper(n, ans):
        if n == 0:
            return ans
        return helper(n - 1, ans * n)
print(factorial(5))'''#this type of code also accepted 


#there are more other six approach is there you can check in ChatGPT

#Generate nth Fibonacci term using recursion.


'''def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

print(fib(5))'''

#Display all array elements using recursion.

'''def display(arr, i=0):
    if i == len(arr):
        return
    print(arr[i])
    return display(arr, i + 1)

display([10, 20, 30, 40, 50])'''


'''def display(arr, i=0):
    if i == len(arr):
        return []
    
    return [arr[i]]+display(arr, i + 1)

print(display([1, 2, 3, 4, 5]))'''
#Find the sum of elements of the array using recursion.


'''def display(arr, i=0):
    if i == len(arr):
        return 0
    
    return arr[i] + display(arr, i + 1)

print(display([1, 2, 3, 4, 5]))'''



