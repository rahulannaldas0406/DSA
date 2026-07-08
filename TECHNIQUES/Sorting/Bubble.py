#Basic Bubble sort

'''arr=[5,3,7,2,8,1]

for i in range(len(arr)):

    for j in range(len(arr)-1-i):

        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]

print(arr)'''

#Sort array in descending order


'''def desc_sort(arr):
    n=len(arr)
    for i in range(n):

        for j in range(n-1-i):
            if arr[j]<arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]


    return arr
a=desc_sort([1,6,4,2,5,3])

print(a)'''


#Print array after each pass

'''def bubble_pass(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

        print("pass",i+1,":",arr)


bubble_pass([5,3,1,4,2])'''

#Count number of swaps

'''def count_swaps(arr):

    count=0

    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                count+=1
    return count
a=count_swaps([6,8,4,2,9,3])

print(a)'''

#Count number of comparisons

'''def count_comp(arr):

    count=0

    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            count+=1
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                
    return count
a=count_comp([6,8,4,2,9,3])

print(a)'''

#Print total passes required

'''def total_passes(arr):

    return len(arr)-1

print(total_passes([6,5,1,2,3,4]))'''

#Find largest element in each pass

'''def largest_ele(arr):
   
    for i in range(len(arr)):
        
        for j in range(len(arr)-1-i):

            if arr[j]>arr[j+1]:
               
                arr[j],arr[j+1]=arr[j+1],arr[j]
                
        print("Pass", i + 1, "Largest:", arr[len(arr) - 1 - i])
largest_ele([6,8,4,2,9,3])'''

#Print index of largest element each pass

'''def largest_idx(arr):
   
    for i in range(len(arr)):
        
        for j in range(len(arr)-1-i):

            if arr[j]>arr[j+1]:
               
                arr[j],arr[j+1]=arr[j+1],arr[j]
                
        print("Pass", i + 1, "Largest:", len(arr)-1-i)
largest_idx([6,8,4,2,9,3])'''

#Sort already sorted array

'''def sorted_bubble(arr):

    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]


    return arr

a=sorted_bubble([1,2,3,4,5])
print(a)'''

#Sort reverse sorted array

'''def reverse_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]


    return arr

a=reverse_sort([5,4,3,2,1])

print(a)'''

#Sort array with duplicates


'''def dupli_ele(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

    return arr

a=dupli_ele([4, 2, 5, 2, 3])
print(a)'''


#Sort array with negative numbers

'''def negative_num(arr):

    negatives = []

   
    for num in arr:

        if num < 0:
            negatives.append(num)

   
    n = len(negatives)

    for i in range(n - 1):

        for j in range(n - 1 - i):

            if negatives[j] > negatives[j + 1]:

                negatives[j], negatives[j + 1] = (
                    negatives[j + 1],
                    negatives[j]
                )

   
    index = 0

    for i in range(len(arr)):

        if arr[i] < 0:

            arr[i] = negatives[index]

            index += 1

    return arr


a = negative_num([-2,-6,3,1,-4,2,0])

print(a)'''


#Sort array with zeros

'''def sort_zeros(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

    return arr

a=sort_zeros([9,3,8,2,0,4,0,1,0,5])

print(a)'''


#Sort array with all equal elements

'''def equal_ele(arr):

    for i in range(len(arr)):
        for j in range(len(arr)-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j],arr[j+1]

    return arr


a=equal_ele([5,5,5,5])

print(a)'''


#Sort only first half of array

'''def half_arr(arr):
    for i in range(len(arr)//2):
        for j in range(len(arr)//2-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

    return arr

a=half_arr([2,5,1,3,4,6])
print(a) '''

#Sort only second half of array

'''def second_half(arr):
    for i in range(len(arr)//2,len(arr)):
        for j in range(len(arr)//2,len(arr)-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

    return arr

a=second_half([5,4,2,1,6,3])
print(a)'''


#Sort first K elements

'''def first_k_ele(arr,k):
    for i in range(k):
        for j in range(k-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

        
    return arr

a=first_k_ele([5,4,3,6,2,1],3)
print(a)'''

#Sort except first element

# from typing import List

# class Solution:
#     def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
#         n = len(rooms)
#         visited = [False] * n
#         visited[0] = True
        
#         # Queue for BFS simulation
#         queue = [0] 
        
#         while queue:
#             current_room = queue.pop(0) # Take the first room
            
#             # Check every key in the current room
#             for key in rooms[current_room]:
#                 if not visited[key]:
#                     visited[key] = True
#                     queue.append(key)
        
#         # Check if all rooms are visited
#         return all(visited)

