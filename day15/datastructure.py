#write a script to print all array values in the console.
'''arr=[1,2,3,4,5]
print(arr)'''

#For the Given array: [23,34,54,0,4,7] print all the Array values using a for loop. Expected output: 23 34 54 0 4 7

'''arr=[23,34,54,0,4,7]
for item in arr:
    print(item,end=" ")'''

'''def arr(a):
    for item in a:
        print(item,end=" ")
arr([1,2,3,4,6])'''

#For the Given array: [23,34,54,10,4,7] print the minimum number in an Array. Expected output: 4

arr=[23,34,54,10,4,7]
'''num=arr[0]
for i in range(0,len(arr)):
    if arr[i]<num:
       num=arr[i]
    
print(num,"is minimum value")'''
#print(min(arr),"minimum number")

#For the Given array: [23,34,54,10,4,7] print the Maximum number in an array. Expected output: 
'''num=arr[0]
for i in range(0,len(arr)):
    if arr[i]>num:
        num=arr[i]
print(num,"maximum number")'''
#print(max(arr),"maximum number")

#For the Given array: [23,34,54,10,4,7] sum of all the numbers in an Array. Expected output: 132
'''num=0
for i in range(0,len(arr)):
    num=num+arr[i]
print(num)'''
#print(sum(arr))

#For the Given array: [23,34,54,10,4,7] Average of all the numbers in an Array. Expected output: 22
'''num=0
for i in range(0,len(arr)):
    num=num+arr[i]
print(num//len(arr))'''

#print(sum(arr)//len(arr))

#CodeGym Community