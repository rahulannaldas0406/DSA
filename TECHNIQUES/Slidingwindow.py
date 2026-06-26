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

