#Sliding window 

#Without sliding window 
'''Algorithm**
1. Set max_sum = 0

2. For each possible starting index:

      Calculate sum of next k elements

      Compare with max_sum

      Update if larger

3. Return max_sum
'''
#bruteforce 

'''def maxSubarraySum(arr, k):

    max_sum = 0

    for i in range(len(arr) - k + 1):

        curr_sum = 0

        for j in range(i, i + k):

            curr_sum += arr[j]

        max_sum = max(max_sum, curr_sum)

    return max_sum


arr = [2,1,5,1,3,2]
k = 3

print(maxSubarraySum(arr, k))'''


#Time complexity is O(n*k) becz inner loop O(k) and outer loop O(n) so finally O(k)*O(n)=O(n*K)


#With sliding window  Tc is O(n)

'''Algorithm**
1.Calculate the sum of the first k elements.
2.Store it as:
    current window sum
    maximum sum
3.Start sliding the window:
    Remove the leftmost element
    Add the new rightmost element
4.Update maximum sum.
5.Repeat until the end.
'''

'''def maxSubarraySum(arr, k):

    window_sum = sum(arr[:k])

    max_sum = window_sum

    for i in range(k, len(arr)):

        window_sum = window_sum - arr[i-k] + arr[i]

        max_sum = max(max_sum, window_sum)

    return max_sum


arr = [2,1,5,1,3,2]
k = 3

print(maxSubarraySum(arr, k))'''

#Maximum Average Subarray I

'''def maxAvgarray(arr,k):
    window_sum=sum(arr[:k])

    max_value=window_sum/k

    for i in range(k,len(arr)):
        window_sum=window_sum-arr[i-k]+arr[i]

        avg_value=window_sum/k
        max_value=max(max_value,avg_value)
    return max_value
arr=[1,12,-5,-6,50,3]
k = 4
print(maxAvgarray(arr,k))'''

#Maximum number of even numbers in a window of size K.

'''arr=[2,1,3,5]
k=2
even_count=0
max_count=0
#first window 
for i in range(k):
    if arr[i]%2==0:
        even_count+=1
max_count=even_count
for i in range(k,len(arr)):
    if arr[i-k]%2==0:
        even_count-=1
    if arr[i]%2==0:
        even_count+=1
    
print(max_count)'''

#Given an array, find the maximum number of negative numbers in any subarray of size k.

'''def max_neg_count(arr,k):
    neg_count=0
    max_count=0
    for i in range(k):
        if arr[i]<0:
            neg_count+=1
    max_count=neg_count

    for i in range(k,len(arr)):
        if arr[i-k]<0:
            neg_count-=1
        if arr[i]<0:
            neg_count+=1
        max_count=max(neg_count,max_count)
    return max_count
arr=[-1,2,-4,5,-2,-5,-6]
k=3
print(max_neg_count(arr,k))'''

for i in range(61,58):
    print(i)