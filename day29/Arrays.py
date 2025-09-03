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

#Find a maximum and minimum element in an array. – using recursion.

    
#Now just normal method 

arr=[3,1,6,2,4,5]


'''arr=[x for x in arr if not isinstance(x,float)]
arr=[x for x in arr if not isinstance(x,bool)]'''


max_temp=0
min_temp=0

for i in range(0,len(arr)):
    

    if arr[i]>max_temp:
        
        max_temp=arr[i]
        

    if arr[i]<min_temp:
        min_temp=arr[i]
#print(second_temp)
'''i=0
while i<len(arr):
    if arr[i]>max_temp:
        max_temp=arr[i]
        
    if arr[i]<min_temp:
        min_temp=arr[i]
    i+=1'''

'''def arr_max_min(arr):
    curr_max=arr[0]
    curr_min=arr[0]
    for i in range(0,len(arr)):
        if arr[i]>curr_max:
            curr_max=arr[i]
        if arr[i]<curr_min:
            curr_min=arr[i]
    return curr_min,curr_max'''


'''i=0
while(i>len(arr)):
    if arr[i]>max_temp:
        max_temp=arr[i]
        i+=1
    else:
        min_temp=arr[i]
        i+=1'''

#print("max number",max_temp)
# print("min number",min_temp)

#print(arr_max_min([-3,-1,-2,2,1]))

'''def rec_max_min(arr):
    if len(arr)==1:
        return arr[0],arr[0]
    cur_max=arr[0]
    cur_min=arr[0]
    rec_max, rec_min = rec_max_min(arr[1:])   # recursion on rest of list

    if arr[0] > rec_max:
        cur_max = arr[0]
    else:
        cur_max = rec_max

    if arr[0] < rec_min:
        cur_min = arr[0]
    else:
        cur_min = rec_min

    return cur_max,cur_min

result = rec_max_min([2, 3, -1, 5, 4])
print(f"(max={result[0]}, min={result[1]})")'''                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             