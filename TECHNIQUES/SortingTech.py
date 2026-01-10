
'''Bubble Sort
Selection Sort
Insertion Sort
Merge Sort
Quick Sort
(and Merge Two Sorted Arrays)'''


#Implement Bubble Sort

#Problem: Write bubble_sort(arr) that sorts arr in ascending order using bubble sort and returns the sorted array.
#Example: [4,2,7,1] → [1,2,4,7]

def bubble_sort(arr):
    
    for i in range(0,len(arr)):
        for j in range(0,len(arr)):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
   return arr
bubble_sort([4,2,7,1,6])
# def bubble(arr):
#     for i in range(0,len(arr)):
#         for j in range(0,len(arr)):

#             if arr[i]<arr[j]:
#                 arr[i],arr[j]=arr[j],arr[i]
                
#     print(arr)

# bubble([4,2,7,1,6])

'''def bubble(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1-i):      # compare until unsorted part
            if arr[j] > arr[j+1]:  # compare adjacent elements
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print(arr)'''



#Count swaps in Bubble Sort (optimization)

#Problem: Using bubble sort, return the number of swaps needed to sort arr. If already sorted return 0.
#Example: [3,2,1] → 3 (3 swaps)

'''def bubble(arr):
    n = len(arr)
    count=0
    for i in range(n-1):
        for j in range(n-1-i):     # compare until unsorted part
            if arr[j] > arr[j+1]:  # compare adjacent elements
                arr[j], arr[j+1] = arr[j+1], arr[j]
                count+=1
                
    print(count)
bubble([4,3,2,1])'''


#selection sort

# def selection_sort(arr):
#     min=0
#     for i in range(len(arr)):
#         for j in range(i+1,len(arr)):
#             if arr[i]>arr[j]:
#                 arr[i],arr[j]=arr[j],arr[i]
#     print(arr)
# selection_sort([3,8,5,7,1,2,4,0])
#find minimum 

'''def selection_sort(arr):
    min=arr[0]
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[j]>min:
                #print("min",arr[j])
                min=arr[j]
                arr[i],arr[j]=arr[j],arr[i]
                #print(arr)
    print(arr)
selection_sort([4,6,2,3])'''


#Insertion sort 
'''arr=[4,2,1,7]
for i in range(1,len(arr)):
    key=arr[i]
    j=i-1
    while j>=0 and arr[j]>key:
        arr[j+1]=arr[j]
        j=j-1
    arr[j+1]=key
print(arr)'''


# i=1

# key=arr[1] #key=4
# j=i-1 #j=1-1 j=0 
# while j>=0 and arr[j]>key #0>=0 and 4>2 
#  arr[j+1]=arr[j] #arr[0+1]=arr[0]; arr[1]=4
#  j=j-1 #0-1 
# arr[j+1]=key #arr[0+1]=4

#merge sort

