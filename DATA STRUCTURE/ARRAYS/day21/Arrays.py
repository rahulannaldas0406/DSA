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

'''arr=[1,1,2,3,4,4,5,2,1]
arr1=[0]*len(arr)
k=0
for i in range(0,len(arr)):
    for j in range(i):
        
        if arr[i]==arr[j]:
            break
    else:
        arr1[k]+=arr[i]
        k+=1
arr1=arr[:k]
print(arr1)'''

#For every basic salary present in the array, add 40% HRA, 92% DA, 10% Tax and display the final output
'''arr=[10000,20000,30000,40000]
arr1=[]
for sal in arr:
    
    hra=sal*0.40
    da=sal*0.92
    tax=sal*0.10
    total=sal+hra+da-tax
    arr1.append(total)
print(arr1)'''

