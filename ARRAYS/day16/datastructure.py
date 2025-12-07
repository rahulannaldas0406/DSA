#For the Given array: [23,34,54,10,34,7,23,10,34] print the total number of times an element found in the array. 
#Given number: 23, Expected output: 2 Given number: 34, Expected output: 3 Given number: 10, Expected output: 2 Given number: 54, 
#Expected output: 1

arr=[23,34,54,10,34,7,23,10,34]
'''target=23
count=0
for items in arr:
    if target==items:
        count+=1
print(count)'''
'''i=0
while i<len(arr):
    if arr[i]==target:
        count+=1
    i+=1
print(count)'''

#For the Given array: [23,34,54,10,34,7,23,10,34] eliminate duplicates in a given array Expected output: 23,34,54,10,7
'''dup={}
arr1=[]
for items in arr:
    if items in dup:
        dup[items]+=1
    else:
        dup[items]=1
for key in dup:
    arr1.append(key)
print(arr1)'''
item=0
dup={}
arr1=[]
while item<len(arr):
    if arr[item] in dup:
        dup[item]+=1
    else:
        dup[item]=1
    item=item+1
keys=list(dup.keys())
j=0
while j<len(keys):
    arr1.append(keys[j])
print(arr1)
