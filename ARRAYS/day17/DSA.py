#For the Given array: [23,-34,-54,10,-4,7] print all the positive numbers in an array. Expected output: 23,10,7

#arr=[23,-34,-54,10,-4,7]
#arr1=[]
'''for item in arr:
    if item>0:
        arr1.append(item)
print(arr1)'''

'''i=0
while i<len(arr):
    if arr[i]>0:
        arr1.append(arr[i])
    i=i+1
print(arr1)'''

#For the Given array: [23,34,54,10,4,7] search if the given number is there in an array or not. Given number: 34, Expected output: true Given number: 26, Expected output: false

# num=34
# for item in arr:
#     if item==num:
#         return True
#     elif item!=num:
#         return  False

'''def check(arr,num):
    for item in arr:
        if item==num:
            return True
    return False
print(check(arr,-34))'''

'''def check_number(arr,num):
    i=0
    while i<len(arr):
        if arr[i]==num:
            return True
        i=i+1
    return False
print(check_number(arr,-34))'''


#For the Given array: [23,34,54,10,34,7,23,10,34] print the total number of times an element found in the array.
#  Given number: 23, Expected output: 2 Given number: 34, Expected output: 3 Given number: 10, Expected output: 2 Given number: 54, Expected output: 1

#arr=[23,34,54,10,34,7,23,10,34]
#count=0
#num=10
'''for item in arr:
    if item==num:
        count+=1
print(num,":",count)'''

'''i=0
while i<len(arr):
    if arr[i]==num:
        count+=1
    i+=1
print(num,":",count)'''


#For the Given array: [23,34,54,10,4,7] print index of a given element in an Array. Given number: 23, 
# Expected output: 0 Given number: 34, Expected output: 1 Given number: 10, Expected output: 3 Given number: 54, Expected output: 2

'''for index in range(0,len(arr)):
    if arr[index]==num:
        print(index)'''

'''i=0
while i<len(arr):
    if arr[i]==num:
        print(i)
    i+=1'''

#Sort an array in ascending order. Given array: [23,34,54,10,4,7] Expected output: 4,7,10,23,34,54 

#bubble sort
arr=[23,34,54,10,4,7]

for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        
        if arr[i]>=arr[j]:
            arr[i],arr[j]=arr[j],arr[i]
print(arr)


'''for i in range(len(arr)):
    min_index=i
    for j in range(i+1,len(arr)):
        if arr[j]<arr[min_index]:
            min_index=j
    arr[i],arr[min_index]=arr[min_index],arr[i]
print(arr)'''

