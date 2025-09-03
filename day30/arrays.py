# t=4
# n=6
# i=1
# pow=n
# while(i<t):
#    pow= pow*n
#    i=i+1
# print(pow)

#just for fun 
'''value="yes"
while(value=="yes"):
    n=int(input("enter a number:"))
    t=int(input("enter power of the number:"))
    pow=1
    for i in range(0,t):
        pow=pow*n
    print(pow)
    value=input("you want to repeat say yes/no:")
print("thank you for your concern :)")'''


#Project Idea: Number Guessing with Binary Search

'''low,high=1,100
while low<=high:
    mid=(low+high)//2
    print("Is it",mid,"?:")
    feedback=input("enter if higher/lower/correct:")
    if feedback=="correct":
        print("i guessed correct it 🎉")
        break
    elif feedback=="higher":
        low=mid+1
    else:
        high=mid-1'''



#Count the total number of even and odd elements in an array.

# arr=[2,5,4,1,8,9,3,7,6]
# count_even,count_odd=0,0


'''for i in arr:
    if i%2==0:
        count_even+=1
    else:
        count_odd+=1'''

#using while loop 

'''i=0
while i<len(arr):
    if arr[i]%2==0:
        count_even+=1
    else:
        count_odd+=1
    i+=1
print(arr)
print("odd number count",count_odd,"even number count",count_even)'''

#Count the total number of negative elements in an array

# arr=[2,4,-1,3,5,-2,-3,6,-6,5,-5,4,-4]
# neg_count=0

'''for i in arr:
    if i<0:
        neg_count+=1
print(neg_count)'''

#using while loop

'''i=0
while i<len(arr):
    if arr[i]<0:
        neg_count+=1
    i+=1
print(neg_count)'''

#Copy all elements from an array to another array.

'''arr=[1,2,3,4,5,6]
cpy_arr=[len(arr)]
j=0
for i in range(len(arr)):
    if j >= len(cpy_arr):          # if index doesn't exist yet
        cpy_arr.append(None)
    cpy_arr[j]=arr[i]
    j+=1
print(cpy_arr)'''

#Insert an element in an array.

#arr=[1,2,3]

#i want to insert more elements

#in simple
'''arr.insert(3,4)
print(arr)'''


#but different way like dynamically

'''arr = [1, 2, 3]
arr = [4] + arr# creates a new bigger list
print(arr)  # [1, 2, 3, 4]'''

#Delete an element from an array at the specified position

'''arr=[1,2,3,4,5]

i want to delete 2 element
del arr[2] #using index
arr.remove(2)
print(arr)'''


#Count frequency of each element in an array.
'''arr=[1,2,3,2,4,3,2]

count_arr={}
for i in arr:
    if i not in count_arr:
        count_arr[i]=1
    else:
        count_arr[i]+=1
for key,value in count_arr.items():
    print(key,"number repeated",value,"times")'''

# from collections import defaultdict

# arr = [1, 2, 3, 2, 4, 3, 2]
# count = defaultdict(int)
# print(count)

#Print all unique elements in the array.

#arr=[1,2,2,3,3,3]

#uniq=set(arr) # using set method
#print(uniq)



# arr = [1, 2, 3, 2, 4, 3, 2]
# unique = set(arr) 
# print(unique)

#Count the total number of duplicate elements in an array.

'''count_arr={}
for i in arr:
    if i not in count_arr:
        count_arr[i]=1
    else:
        count_arr[i]+=1
count=0
for key,value in count_arr.items():
    if value>1:
        count+=1
print(count)'''

#Get the second largest element in an array.
arr=[3,1,2,4]



'''for i in range(0,len(arr)):
    second_ele=arr[1]
    if arr[i]<second_ele:
        pass
    else:
        second_ele=arr[i]
print(second_ele)'''

#Merge two arrays to the third array.

'''arr1=[1,2,3]
arr2=[4,5,6]
arr3=[]'''

#print(arr1+arr2)
'''for i in arr1:
    arr3.append(i)
for j in arr2:
    arr3.append(j)
print(arr3)'''

#Find the reverse of an array.

arr=[5,1,3,4,2,7]
high=0
low=len(arr)-1
'''for i in range(0,len(arr)//2):
    arr[high],arr[low]=arr[low],arr[high]
    high+=1
    low-=1

print(arr)'''

#now using while loop

'''i=0
while i<len(arr)//2:
    arr[high],arr[low]=arr[low],arr[high]
    high+=1
    low-=1
    i+=1
print(arr)'''
