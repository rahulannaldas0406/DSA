#Starts Variable Size Window 

#Longest Subarray With Sum ≤ K

'''def variblesize(arr,k):
    left=0
    window_sum=0
    max_len=0

    for right in range(len(arr)):
        window_sum+=arr[right]
        

        while window_sum>k:
            window_sum-=arr[left]
            left+=1
        max_len=max(max_len,right-left+1)

    return max_len

arr=[2,1,3,5,4]
k=7
print(variblesize(arr,k))'''

#Longest Substring Without Repeating Characters

'''def longest_subStr(s):
    left=0
    window=set()  # I missed up here to find set or add 
    max_len=0
    for right in range(len(s)):
    
        while s[right] in window:
            window.remove(s[left])
            left+=1

        window.add(s[right])

        max_len=max(max_len,right-left+1)
    return max_len

s="abcabcbb"
print(longest_subStr(s))'''

#Not update 

#same as like ystr
