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
    return helper(n, 1)

print(factorial(5))'''


#there are more other six approach is there you can check in ChatGPT

#Generate nth Fibonacci term using recursion.


'''def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

print(fib(5))'''

#Display all array elements using recursion.

def arr_ele(n):

