#For the Given array: [23,-34,-54,10,-4,7] print all the positive numbers in an array. Expected output: 23,10,7

arr=[23,-34,-54,10,-4,7]
arr1=[]
for item in arr:
    if item>0:
        arr1.append(item)
print(arr1)