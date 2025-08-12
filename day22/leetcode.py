'''arr=[0,4,3,0,6,0]
arr1=[]
for i in arr:
    if i==0:
        arr.remove(i)
        arr1.append(i)
print(arr+arr1)'''      


'''def movezero(nums):
    arr1[]=nums
    arr=[]
    for i in nums:
        if i==0:
            nums.remove(i)
            arr.append(i)
    return arr
n=[0,1,2,4,0,3]
movezero(n)'''
#Eliminate duplicates from a array

'''arr=[1,1,2,3,4,4,5,2,1]
arr1=[]
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]==arr[j]:
            break
    else:
        arr1.append(i)
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

#For every salary, deduct 10% tax for salaries less than 50000 and deduct 12% tax for salaries more than 50000

'''arr=[10000,20000,50000,60000,70000]
total=[]
for sal in arr:
    more=sal*0.12
    less=sal*0.10
    if sal>50000:
        tot=sal-more
        total.append(tot)
    else:
        tot=sal-less
        total.append(tot)
print(total)'''

#Insert first 10 odd numbers in an empty array(for and while).

arr=[]
count=0
for i in range(0,100):
    if count==10:
        break
    if i%2!=0:
        count+=1
        arr.append(i)

print(arr)
