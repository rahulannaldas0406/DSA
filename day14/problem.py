'''for i in range(1,6):
    for j in range(i,6):
        print(" ")
        for k in range(i,j):
            print("*",end="")'''
'''for i in range(1,6):
    print("")
    for j in range(2,6):
        for k in range(i,6):
            print("*",end="")'''
arr=[1,2,3,4,5,6,7,10,15]
newarr=[0]*len(arr)
for i in range(0,len(arr)):
    #print(arr[i])
    newarr[i]=arr[i]
    if newarr[i]%3==0 and newarr[i]%5==0:
        newarr[i]="fizz buzz"
    elif newarr[i]%3==0:
        newarr[i]="fizz"
    elif newarr[i]%5==0:
        newarr[i]="buzz"
    else:
        newarr[i]=str(arr[i])
        
print(newarr)