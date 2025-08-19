#Remove duplicates from sorted array
'''Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).'''

arr=[1,1,2,3,3]
# # arr1=[]
# dup={}
# arr1=[]
# for items in arr:
#     print(dup[items])
#     if items in dup:
#         dup[items]+=1
#     else:
#         dup[items]=1
# for key in dup:
#     arr1.append(key)
# for i in arr1:


'''i=0
for j in range(1,len(arr)):
    if arr[j]!=arr[i]:
        i+=1
        arr[i]=arr[j]
print(i)
for k in range(i+1,len(arr)):
    arr[k]="_"
print(arr)'''

#Reduce the each element of the array by 25% and store in a separate array

'''arr=[100,200,300,400]

print([item*0.75 for item in arr])'''

'''arr=[100,200,300,400]
i=0
print(while arr[i]*=0.75 i+=1)'''

#Store only even numbers of a given array in another array.

'''arr=[1,2,3,4,5,6,7]
arr1=[]
for i in arr:
    if i%2==0:
        arr1.append(i)
print(arr1)'''


#create a duplicate array for a given array.

'''arr=[1,2,3,4,5]

for i in arr:
    arr.append(i)
print(arr)'''

val=2
i=0
for j in range(1,len(arr)):
    if arr[j]==val:
        break
    else:
        i+=1
        arr[i]=arr[j]
for k in (i+1,len(arr)):
    arr[k]="_"
print(arr)
