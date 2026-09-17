#Sum of all array elements. – using recursion.

#before this we should earn what is recursion 

#example

'''def facorial(n):
    if n==1:
        return 1
    else:
        return n*facorial(n-1)
print(facorial(5))'''

#so in between (*) we put (+) it work sum so as like we can write sum a array look 
 
#arr=[1,2,3,4]

def sum_arr(arr):
    
    if len(arr)==1:
        return arr[0]
    else:
        return arr[0]+sum_arr(arr[1:])
print(sum_arr([1,2,3,4]))
