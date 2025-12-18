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