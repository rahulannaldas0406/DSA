#ARRAYS

#In leetcode problem 167


#Solution 
'''def twoSum(numbers, target):
    left,right=0,len(numbers)-1
    result=[]
    while left<right:
        s = numbers[left] + numbers[right]
        if s==target:
            return [left+1,right+1]
            break
        elif s<target:
            left+=1
        else:
            right-=1
    return result'''

# It is Type two in pointer Technique

'''def duplicateElement(arr):
    if len(arr)==0:
        return 0
    
    slow=0
    for fast in range(1,len(arr)):
    
        if arr[fast]!=arr[slow]:
            slow+=1
            arr[slow]=arr[fast]
    return slow+1
arr=[1,1,2,2,3]
k=duplicateElement(arr)
print(arr[:k])'''


#Day1
#5 problems (Beginner to Easy level)

#Check if array has pair with given sum (sorted) 

'''arr=[1,2,3,4,6]
k=6
i=0
j=len(arr)-1
while i<j:
    if arr[i]+arr[j]>k:
        j-=1
    elif arr[i]+arr[j]<k:
        i+=1
    else:
        print(i,j)
        break'''

#Reverse a string 

'''a="rahul" #string is a immutable
a=list(a) #important line must convert into list 
i=0
j=len(a)-1

while i<j:
    a[i],a[j]=a[j],a[i]
    i+=1
    j-=1

a="".join(a)
print(a)'''


#Remove duplicates from sorted array 

'''arr=[1,1,2,2,3]

slow=0
for fast in range(1,len(arr)):
    if arr[fast]!=arr[slow]:
        slow+=1
        arr[slow]=arr[fast]
print(arr[:slow+1])'''

#Check palindrome string 

'''a="madAm"
a=a.lower() # in there is string mixed characters 
a=list(a)
first=0
last=len(a)-1
res=False
while first<last:
    if a[first]==a[last]:
        res=True

    else:
        res=False
        break
    first+=1
    last-=1
print(res)'''

#Move all zeros to end 

'''arr=[1,0,2,0,3,0,4,0,6]

first=0
for last in range(len(arr)):
    if arr[first]==0 and arr[last]==0:
        pass
    elif arr[first]!=0:
        first+=1
    else:
        arr[first],arr[last]=arr[last],arr[first]
        first+=1

print(arr)'''

# this is correct but there is time and space complexity is more 
#Type 2

'''arr=[1,0,2,0,3,0,4]

slow=0
for fast in range(len(arr)):
    if arr[fast]!=0:
        arr[slow],arr[fast]=arr[fast],arr[slow]
        slow+=1
print(arr)'''

#<-----Mission Completed!----->


#Day 2
#Easy level to Medium level

#Reverse a vowels in string (leetcode problem:345)
'''Example: a=rahul output:ruhal'''

'''a="IceCreAm"
vow="aeiouAEIOU"
a=list(a)
first=0
last=len(a)-1
while first<last:
    if a[first] in vow:
        if a[last] in vow:
            a[first],a[last]=a[last],a[first]
            first+=1
            last-=1
        else:
            last-=1
    elif a[last] in vow:
        first+=1
    else:
        first+=1
        last-=1
a="".join(a)
print(a)'''

#Remove Element (in place)

'''Example: nums=[3,2,2,3],val=3 output:2,nums=[2,2,_,_]'''

'''arr=[3,2,2,3]
val=3
for i in range(0,len(arr)):'''
    


#Day 3 started after long time

#medium problem 

'''1️⃣ Container With Most Water (MUST)
2️⃣ 3Sum (if time)'''


'''container problem will take time beacuse didn't understanding the problem  b '''

#Break for mids!
'''nums = [9,4,1,7]
nums.sort()
i=0
j=1
res=nums[-1]
while i<len(nums) or j<len(nums)-1:
    diff=nums[j]-nums[i]
    if diff<res:
        res=diff
    i+=1
    j+=1
    
print(res)'''

#container with most water 

'''def maxArea(height):
        n=len(height)
        lp=0
        rp=n-1
        max_wt=0
        curr_wt=0
        while lp<rp:
            ht=min(height[lp],height[rp])
            width=rp-lp
            curr_wt=ht*width
            max_wt=max(curr_wt,max_wt)
            if height[lp]<height[rp]:
                lp+=1
            else:
                rp-=1
        return max_wt'''








