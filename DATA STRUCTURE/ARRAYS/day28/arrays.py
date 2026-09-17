#insert An Element Desired or Specific Position In An Array

#arr=[1,2,3,4,6]

#i want insert 6 element at 4 index 

'''arr.insert(4,5)
print(arr)'''

#arr=[1,2,3,2,1,5,3,2,4]

'''unique_array=list(set(arr))
print(unique_array)'''

'''unique_array=list(dict.fromkeys(arr))
print(unique_array)'''

'''unq_arr=[]
for i in arr:
    if i not in unq_arr:
        unq_arr.append(i)
print(unq_arr)'''

#Delete Element From Array At Desired Or Specific Position 

#arr=[1,2,3,3,4,5,6]

'''arr.remove(3)
print(arr)'''

'''del arr[2]
print(arr)'''

'''remove=arr.pop(2)
print(arr)
print("removed",remove)'''

#Check String Is Palindrome Or Not Using For Loop


'''str="mada"

str1=""
for i in range(len(str),-1,-1):
    str1=str1+str[i]
if str==str1:
    print("it is palindrome")
else:
    print("it is not palindrome")'''

'''if "str"=="str":
    print("hi")
else:
    print("hello")'''

#nums=[3,2,2,3]
'''val=3
k=0
for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k+=1

print(nums[:k])'''

'''arr=[2,2]
arr1=[]

for i in range(0,len(nums)):
    arr1.append(arr[i])
print(arr1)'''

nums = [3,2,2,3]
val = 3
k = 0

for i in range(len(nums)):
    if nums[i] != val:
        nums[k] = nums[i]
        k += 1

# Fill the rest with a special placeholder `_`
for j in range(k, len(nums)):
    nums[j] = "_"

# Pretty print without quotes
print("[" + ", ".join(str(x) if x != "_" else "_" for x in nums) + "]")
