#Problem: Given an array arr and a value x, return the index of x in arr. If not found, return -1.
#Example: arr = [4, 1, 7, 3], x = 7 → output 2 (0-based index)

'''def liner_search(arr,x):
    for i in range(len(arr)):
        if arr[i]==x:
            return i
    else:
        return -1
var=liner_search([1,2,3,5,4,6],5)
print(var)'''

#Problem: Given a sorted array arr (ascending) and x, return index of x else -1.
#Example: arr = [1,3,5,7,9], x = 5 → 2

'''def binary_search(arr,x):
    lo, hi=0 , len(arr)-1
    
    while lo<=hi:
        mid=lo+(hi-lo)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]<x:
            lo = mid+1
        else:
            hi=mid-1

    return -1
var=binary_search([1,3,5,7,9],7)
print(var)'''

#Problem: In sorted array arr find the first and last index of x. If not present return (-1,-1).
#Example: arr=[1,2,2,2,3], x=2 → (1,3)

'''def first_occurance(arr,x):
    lo,hi=0,len(arr)-1
    ind=-1
    while lo<=hi:
        mid=lo+(hi-lo)//2
        if arr[mid]==x:
            ind=mid
            hi=mid-1
        elif arr[mid]<x:
            lo=mid+1
        else:
            hi=mid-1
    return mid

def last_occurance(arr,x):
    lo,hi=0,len(arr)-1
    ind=-1
    while lo<=hi:
        mid=lo+(hi-lo)//2
        if arr[mid]==x:
            ind=mid
            lo=mid+1
        elif arr[mid]<x:
            lo=mid+1
        else:
            hi=mid-1
    return mid
def first_last(arr,x):
    return (first_occurance(arr,x),last_occurance(arr,x))

var=first_last([1,2,2,2,3,4],2)
print(var)'''

#Problem: Count how many times x appears in sorted arr.
#Example: [1,2,2,3,2] (if unsorted) — but prefer sorted arrays for binary technique. If sorted [1,2,2,2,3] and x=2 → 3.

'''def count(arr,x):
    count=0
    i=0
    while i<len(arr):
        if arr[i]==x:
            count+=1
        i+=1
    return count
var=count([1,2,2,3,2,4,5],2)
print(var)'''

#Problem: Given array where arr[i] != arr[i+1] and it increases then decreases (mountain), find index of peak (maximum). Works even if not strict mountain — general local peak find.
#Example: [1,3,5,4,2] → 2 (value 5)

'''def find_peak(arr):
    lo,hi=0,len(arr)-1  #lo=0, hi=4
    while lo<hi:
        mid=lo+(hi-lo)//2  #mid=0+(4-0)//2=2 # mid=3
        if arr[mid]<arr[mid+1]: #arr[2]<arr[3] # arr[3]<arr[4]
            lo=mid+1 #lo=3
        else:
            hi=mid #hi=3.5
    return lo
var=find_peak([3,5,4,2,1])
print(var)'''

 