#Store only even numbers of a given array in another array.

'''arr=[1,2,3,4,5,6]
arr1=[]
for i in arr:
    if i%2==0:
        arr1.append(i)
print(arr1)'''

#create a duplicate array for a given array.

arr=[1,2,3,4,5]

'''for i in arr:
    arr1.append(i)
print(arr1)'''

#arr1=arr[:] we can also write duplicate array using slicing 

#arr1=arr[::-1] we can write like this in reverse of a array
#print(arr1)

'''And also we can write differnet ways:
 for example :-  using constructor list(arr) 
                  using arr.copy()'''

#Eliminate duplicates from a array

arr=[1,1,2,3,4,4,5,2,1]
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if arr[j]==arr[i]:
            arr.remove(arr[j])
print(arr)