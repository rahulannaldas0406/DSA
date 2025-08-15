'''def sum():
    mssg="messg"
    def inner():
        mssg="hi"
        pass
    inner()
    print("mssg:",mssg)
sum()'''

#Write a program to remove elements from an array which are not in the ascending order 
# Ex: Original array: [12,34,11,56,37,98,23,67,109,45] Output : [12,34,56,98,109]
 
'''def remove(a):
    arr=a
    i=0
    while i<len(arr):
        if arr[i]>arr[i+1]:
            pass
        else:
            arr.remove(arr[i])
        i+=1c
    return arr
ele=remove([12,34,11,56,37,98,23,67,109,45])
print(ele)'''

arr=[12,34,11,56,37,98,23,67,109,45]
arr1=[]
i=0
arr1.append(arr[i])
while i<len(arr):
    
    if arr1[i]<arr[i+1]:
        arr1.append(arr[i+1])
    else:
        arr.remove(arr[i+1])
    i+=1
print(arr)
