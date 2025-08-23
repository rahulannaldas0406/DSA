#Convert All Input String Simultaneously Into Asterisk ( * )

#only logic
'''str="hello"
for i in str:
    print("*",end="")'''

#Now using function 

'''def Astrik(n):
    if len(n)==0:
        print("")
    for i in n:
        print("*",end="")
Astrik("")'''

#return function

'''def Astrik(n):
    if len(n)==1:
        return ""
    
    return "*" *len(n)
print(Astrik("string"))
print(Astrik(" "))'''

#Read and print elements of the array. – using recursion.


'''def read(n):
    if len(n)==0:
        return 
    print(n[0],end="")
    read(n[1:])
print(read([1,2,3,4,5]))'''

#Print all negative elements in an array.

'''arr=[1,-3,4,-5,-2,7,-1]
for i in arr:
    if i<0:
        print(i)'''

#Sum of all array elements. – using recursion.

'''def sum_arr(arr):
    
    if len(arr)==1:
        return arr[0]
    else:
        return arr[0]+sum_arr(arr[1:])
print(sum_arr([1,2,3,4]))'''
