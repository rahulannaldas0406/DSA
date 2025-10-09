#For the Given array: [23,34,54,0,4,7] print all the Array values using a for loop. 
# Expected output: 23 34 54 0 4 7

'''def cout(num):
    for i in num:
        print(i,end=" ")
arr=[23,34,54,0,4,7]
cout(arr)'''
#print all numbers in an array except the first element. Expected output: 34 54 0 4 7

def cout(num):
    for i in range(0,len(num)):
        if i!=0:
            print(num[i],end=" ")
arr=[23,34,54,0,4,7]
cout(arr)